from common import *
import sys
import shutil

from python_git_wrapper import Repository

USE_MAVEN = True


if __name__ == "__main__":
    actions = ("setup", "makePatches", "applyPatches")

    if len(sys.argv) <= 1 or sys.argv[1] not in actions:
        print("Usage: python run.py [{}]".format("|".join(actions)))
        sys.exit(1)

    action = sys.argv[1]
    pre_init()

    if action == "setup":
        if Constants.PROJECT_DIR.is_dir():
            print("Project directory already exists. Please delete the folder and run setup again.")
            sys.exit(1)

        # remove previous work dir
        shutil.rmtree(Constants.WORK_DIR, ignore_errors=True)
        Constants.ensure_dirs()

        # download and decompile
        jar_path = Constants.DOWNLOADS_DIR / "minigui.jar"
        download_server_jar(jar_path)

        decompile(jar_path, Constants.DECOMPILE_DIR)

        # TODO: apply patches after setup

        # initialize project directory
        if not USE_MAVEN:
            # raw intellij build system:
            Constants.PROJECT_DIR.mkdir(parents=True, exist_ok=True)
            src = Constants.PROJECT_DIR / "src"
            src.mkdir(parents=True, exist_ok=True)
        else:
            # Maven initialization:
            # mvn archetype:generate -DgroupId=com.hypixel.hytale -DartifactId=hytale-server -DarchetypeArtifactId=maven‑archetype‑quickstart -DinteractiveMode=false
            logger.info("\n\nInitializing Maven project in:\n{}\n\n", Constants.PROJECT_DIR)

            subprocess.run([
                "mvn", "archetype:generate",
                # "-DgroupId=com.hypixel.hytale", "-DartifactId=hytale-server",
                "-DgroupId=dev.ribica.hytalemodding", "-DartifactId=" + Constants.PROJECT_DIR.name,
                "-DarchetypeArtifactId=maven-archetype-quickstart", "-DinteractiveMode=false"
            ], check=True, shell=True)

            logger.info("Maven project initialized!")

            src = Constants.PROJECT_DIR / "src" / "main" / "java"

        shutil.rmtree(src)
        shutil.copytree(Constants.DECOMPILE_DIR, src)

        repo_gitignore = Constants.PROJECT_DIR / ".gitignore"
        repo_gitignore.write_text("\n".join(("target/", ".idea/", "out/", "*.iml", "*.class")))

        repo = Repository(str(Constants.PROJECT_DIR))
        repo.add_files(all_files=True)
        repo.commit("Initial decompilation")



        print(repo)


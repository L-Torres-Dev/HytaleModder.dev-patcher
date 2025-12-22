from common import *
import sys
import shutil


if __name__ == "__main__":
    actions = ("setup", "makePatches", "applyPatches")

    if len(sys.argv) <= 1 or sys.argv[1] not in actions:
        print("Usage: python run.py [{}]".format("|".join(actions)))
        sys.exit(1)

    action = sys.argv[1]
    pre_init()

    if action == "setup":
        # remove previous work dir
        shutil.rmtree(Constants.WORK_DIR, ignore_errors=True)

        # download and decompile
        jar_path = Constants.DOWNLOADS_DIR / "minigui.jar"
        download_server_jar(jar_path)

        decompile(jar_path, Constants.DECOMPILE_DIR)

        # TODO: apply patches after setup

        # initialize project


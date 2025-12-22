# Patcher

This patcher allows you to more easily prepare an environment for exploring the Hytale Server without publishing the decompiled code.




## Setup

* Clone this repository and `cd` into it.

* Create a Python virtual environment in the `.venv` folder. The command for this varies by platform but it is probably 
one of these: 
  - `python -m venv .venv`
  - `python3 -m venv .venv` (Linux)
  - `py -3.13 -m venv .venv` (Windows)  

  In the last one, specifying the version is recommended if you have multiple Pythons installed.

* Activate the virtual environment:
  - Windows: `".venv\Scripts\activate"`  (including the quotes)
  - Linux/Mac: `source .venv/bin/activate`

## Contributing (work in progress)

1. Decompile the server jar in `/work/decompile`
2. Run the `applyPatches.py` file to apply the current patches
3. Make any changes you wish to the code such as adding new documentation etc.
4. Run the `makePatches.py` and commit that code to your fork.
5. You can now make a PR and get these patches merged to the repository.

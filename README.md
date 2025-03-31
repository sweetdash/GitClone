# GitClone - Python Git Implementation

This project aims to replicate basic Git version control functionality using Python. Currently, the implementation focuses on the initialization feature.

## Project Structure

The project is organized as follows:

## File Descriptions

* **`mygit/__init__.py`**: An empty file that makes the `mygit` directory a Python package.
* **`mygit/init.py`**: Contains the code responsible for initializing a new Git repository (`git init`).
* **`main.py`**: The main entry point for the GitClone command-line interface (CLI).
* **`workspace/`**: The user's working directory where files to be tracked are located.
* **`.mygit/`**: The hidden directory that stores all the Git repository's metadata.
    * **`.mygit/objects/`**: Stores the content of files (blobs) and commit objects.
    * **`.mygit/refs/`**: Stores references to commits, branches, and tags.
        * **`.mygit/refs/heads/`**: Stores references to local branches.
    * **`.mygit/HEAD`**: Points to the currently checked-out branch.
* **`requirements.txt`**: Lists the Python dependencies required for the project (if any).
* **`README.md`**: This file, providing information about the project.

## Functionality (Current)

* **Repository Initialization (`git init`):**
    * The `init.py` module creates the `.mygit` directory structure, setting up the necessary files and folders for version control. This includes creating the `objects`, `refs/heads`, and `HEAD` files.

## Current Status

* As of now, only the repository initialization feature is implemented.
* The project is still under development, and the tracking of workspace changes is yet to be implemented.

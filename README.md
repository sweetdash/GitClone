# GitClone

I am attempting to Clone the git's version control using python. Well for now I have only implemented the initialization fetaure.
The file structure for this project for now is like this:-
mygit_project/            
│── mygit/                # Main package for our Git system
│   │── __init__.py       # Makes mygit/ a package
│   │── init.py           # Handles repository initialization
│── main.py               # Entry point for MyGit CLI

# AND I still have to figure out how to track the certain workspace I need.

│── workspace/            # User's working directory (tracked files)
│── .mygit/               # Hidden folder for version control
│   │── objects/          # Stores file snapshots (like Git blobs)
│   │── refs/             # Stores branch references
│   │   ├── heads/        # Stores branch names and commit pointers
│   │── HEAD              # Points to the current branch
│── requirements.txt      # Dependencies (if needed)
│── README.md           

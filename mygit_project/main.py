import sys
from mygit.init import init # importing init from init.py file under mygit

def main():
    """Entry point for MyGit command-line interface."""
    if len(sys.argv)<2:
        print("Wrong usage. python main.py <command>")
        return
    command=sys.argv[1]

    if command=="init":
        init()
    else:
        print(f"Unknown command : {command}")
if __name__ =="__main__": # this ensures that the "main" logic is defined only when the main.py program is executed directly. if it is getting imported the main logic wont get executed.
    main()
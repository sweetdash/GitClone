import os

def init():
     """Initialize a MyGit repository by creating necessary directories and files."""
     if os.path.exists(".mygit"): # checks for the presence of the .mygit file in the working directory
          print("Repository already initialized")
          return #if present no need to initialize a new one
     
     ''' well os.mkdirs will make sure that the folders mentioned in the () are created. If not they wil create them. '''
     os.makedirs(".mygit/objects",exist_ok=True) # exist_ok checks if the file already exists. If it exists then do nothing, else create the file.
     os.makedirs(".mygit/refs/heads",exist_ok=True) # exist_ok checks if the file already exists. If it exists then do nothing, else create the file.

     with open(".mygit/HEAD","w") as f: # if the file is created then it will be overridden 
        f.write("ref: refs/heads/main\n")
     print("Initialized empty MyGit repository in .mygit")
        
    

if __name__=="__main__":
     from mygit import init 
     import sys
     if len(sys.argv)>1 and sys.argv[1] == "init":
          init()

import subprocess
import os

def upload_to_github():

    fileName=input('Enter the file name:')

    repo_name=input('Enter the Github repository link:')

    commit_message=input('Enter the commit message:')
        
  # Initialize a Git repository in a temporary directory

    subprocess.run(['git','init'])
    
   #set the remote repository URL in your local Git repository

    subprocess.run(['git','remote','add','origin',repo_name])
   
    # Add the file to the staging area

    subprocess.run(['git','add',fileName])

    # Commit the changes

    subprocess.run(['git','commit','-m',commit_message])

    # Push the changes to the origin master branch

    subprocess.run(['git','push','origin','master'])

    print('Contributed :)')


upload_to_github()

# Echo Air Monitor
For our team's project, we have been tasked with creating a system that displays air quality in the City of Aberdeen and saves the data for archiving and analysis of quality changes over time. 

## What is this file?
This file is the Maintenance Manual that will tell you everything you need to know to use this program
It will detail installation, functionality, testing and what is required to keep the program working as intended.

#### Things to be aware of
- This program runs in Python and uses the Django framework
- It was built using Codio as its compiler so the instructions will be based on Codio's functionality and may need to be adjusted to you preferred program
- Some areas such as the APIs and DataPull source may not be active when you access this system so may need to be altered for use

  
## Requirements
The libraries needed for this are contained within the 'requirements.txt' file.
The most important of these libraries are the following and are all installed by the **pip install <library name>** command:
- Django | *A*
- behave | *B*
- whitenoise | *C*
- gunicorn | *D*

## Building the application
 What steps are there to build this application?
- **git init** | *A*
- **git clone git@github.com:Xenterra/GroupProjectBackup.git** | *A*
- **source .venv/bin/activate** | *A*
- **pip install --upgrade pip** | *A*
- **pip install -r requirements.txt** | *A*
- **python3 manage.py runserver 0.0.0.0:2500** | *A*

## Deploying the application
- **pip install heroku** | *First set up Heroku within your project
- **curl https://cli-assets.heroku.com/install.sh | sh** | *Backup method of Heroku installation if the pip install fails*
- **heroku login -i** | *Here you will be able to login to Heroku and access apps with your account* ***HOWEVER, this may act differently on some compilers***
- **heroku create -a <app name on Heroku>** | *If this is a new app on Heroku, you will need to create one*
- **heroku git:remote -a <app name on Heroku>**	| *used to set up a connection between git and an existing Heroku app*
- **heroku config:set DISABLE_COLLECTSTATIC=0**  | *using either 0 or 1 to turn the function on or off for static integration, e.g. for image upload*
- **git push heroku master** | *A*

## Testing the build
How do I test the code to ensure the build is correct?
### Behave
  
## Running the application
- **python3 manage.py DataPull**

### Important Commands
- **pip freeze > requirements.text** | *This command will create the txt file that records pip module versions, mainly for Heroku.*
- **python3 manage.py makemigrations** | *Prep the system for changes to the models.py file. (Required for the next command to work)*
- **python3 manage.py migrate** | *Implement changes from the model.py file into the system.*

#### Git Commands
- **git status** 							| *check the current status of the GitHub repository*
- **git add .**               | *add changes to the local version of the app*
- **git commit -m "update"**  | *save changes made to the local repository in preparation for upload*
- **git push origin master**  | *push your changes to the master branch of the repository*
- **git pull origin master**  | *pulls any changes from the repository from GitHub ! DO THIS BEFORE EDITING YOUR OWN WORK*

## Team Members
 Who's working on this application?

## Future Goals
 Add something about what the application will do when more complete

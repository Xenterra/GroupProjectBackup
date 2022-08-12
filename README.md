# Echo Air Monitor
For our team's project, we have been tasked with creating a system that displays air quality in the City of Aberdeen and saves the data for archiving and analysis of quality changes over time.

## What is this file?
This file is the Maintenance Manual for the application, and will tell you everything you need to know to use this program.
It will detail installation, functionality, testing and what is required to keep the program working as intended.

#### Things to be aware of
- This program runs in Python and uses the Django framework.
- It was built using Codio as its compiler so the instructions will be based on Codio's functionality and may need to be adjusted to you preferred program.
- Some areas such as the APIs and DataPull source may not be active when you access this system so may need to be altered for use.

## Requirements
The libraries needed for this are contained within the 'requirements.txt' file. 
The most important of these libraries are the following and are all installed by the **pip install <library name>** command:
- Django     | *This is the library for the Web Framework used to build the site*
- behave     | *This library handles the automated testing for the system*
- whitenoise | *This one is used for uploading images and larger files to Heroku*
- gunicorn   | *This is the web server library for Python*

## Building the application
 Follow these steps, in order, in the **Terminal** your preferred compiler to build the project:
- **git init**                                                 | *This is the first command that prepares the file for a Git project*
- **git clone git@github.com:Xenterra/GroupProjectBackup.git** | *Use this to pull everything from this repository to you local device*
- **source .venv/bin/activate**                                | *Once you've pulled everything, use this to activate the virtual environment*
- **pip install --upgrade pip**                                | *With the environment active, use this command to make sure that the 'pip' module is up-to-date*
- **pip install -r requirements.txt**                          | *This one will install of the listed pips within the requirements file*
  - ***NOTE: there may be outdated libraries listed in this file, your compiler should inform you of these errors.*** 
- **python3 manage.py runserver 0.0.0.0:2500**                 | *Use this when the virtual environment is active to run the server on your localhost* ***port 2500*** 
  - ***This program is designed to run in Chrome. Open a browser tab and enter '0.0.0.0:2500' in the top bar to see the web app***
  - *You can change the port to whatever number you need*

## Deploying the application
Below are the steps to deploy the web app to Heroku. 
*If you wish to deploy it using another service, follow a guide for that webservice's instructions*.
- **pip install heroku**                                 | *First set up Heroku within your project
- **curl https://cli-assets.heroku.com/install.sh | sh** | *Backup method of Heroku installation if the pip install fails*
- **heroku login -i**                                    | *Here you will be able to login to Heroku and access apps with your account* 
  - ***HOWEVER, this may act differently on some compilers***
- **heroku create -a <app name on Heroku>**              | *If this is a new app on Heroku, you will need to create one*
- **heroku git:remote -a <app name on Heroku>**	         | *Used to set up a connection between Git and an existing Heroku app*
- **heroku config:set DISABLE_COLLECTSTATIC=0**          | *Using either 0 or 1 to turn the function on or off for static integration, e.g. for image upload*
- **git push heroku master**                             | *This is the command used to push changes through Git and into Heroku.* 
  - ***Only use after the push git command***

## Testing the build
By the end of the 'Build' instructions you should see a working website, provided all has gone well. 
Should the compiler return the code running as intended, but nothing is displayed; follow these steps to test the application.

#### Behave
This application has built-in, automated tests that should check the functionality of the website.
It will also use some 'summy data' to confirm that everything is processing as expected.
In you compiler's Terminal type the command '**behave**' and the system should automatically run 4 tests.
- Test 1: Will check that the system can reach the comparison page
- Test 2: This test will check that the website gets to the List Page and that there is data present
- Test 3: This test will follow the pathing of Test 2, then check that it can acces the details of one sensor
- Test 4: The final test will confirm the Map Page is functional, and that it can access a sensor on the map
  - ***WARNING: At the time of writing this manual this test is broken and cannot succeed***

## Running the application
For the management of this system, there are 4 commands that all do the same thing. 
Most of them are old iterations that are kept in for troubleshooting issues. 'DataPull.py' is the most up-to-date one.
- **python3 manage.py DataPull** | *This is the only command of note, it is used to pull the data from the target source.*

### Important Commands
- **pip freeze > requirements.text**   | *This command will create the txt file that records pip module versions, mainly for Heroku.*
- **python3 manage.py makemigrations** | *Prep the system for changes to the models.py file. (Required for the next command to work)*
- **python3 manage.py migrate**        | *Implement changes from the model.py file into the system.*

#### Git Commands
- **git status** 							| *check the current status of the GitHub repository*
- **git add .**               | *add changes to the local version of the app*
- **git commit -m "update"**  | *save changes made to the local repository in preparation for upload*
- **git push origin master**  | *push your changes to the master branch of the repository*
- **git pull origin master**  | *pulls any changes from the repository from GitHub ! DO THIS BEFORE EDITING ON YOUR DEVICE*

## Additional Requirements
In the file: **/airMonitor/views.py**; there are some lines that will need to adjusted to change the current API connections:
 - 81 - This line handles the URL of the target API and may need to change if the API ceases function, or needs updated.
 - 86 & 87 - Likewise, these are the 'Key' and 'Host Address' of the API and will need to change to match the above URL.

Similarly, in the file: /airMonitor/management/commands/DataPull.py;
- 23 - This line contains the URL of the 'Data Source JSON' file and will need to be adjusted to match your personal requirements.
 
## Team Members
  - Joshua Drage - 52102761
  - Adwoa Serwa Addai - 52105349
  - Tongwei Shi - 54104510
  - Wen FANG - 50078152
  - Yunhao Yang - 52104330

## Future Goals
 ### Bug Fixes
 - Repair Test 4 functionality
 - Update Reuirements file automatically over time
 
 ### Improvements
 - Additional options for the Search Bar
 - 3D Map to improve visualisation
 - Live Weather Displayed directly on the map
 - Worldwide Sensor Array
 - Additional Charts on the Details Pages

# TaskMaster

## Description
TaskMaster is a Python application that helps users manage their daily tasks effectively.

Many people struggle to track their tasks and may forget important deadlines or appointments, causing stress and potentially negative consequences. This application provides an easy-to-use interface that allows users to create, update, and delete tasks and set deadlines.

The application uses Python's built-in library TKinter for the graphical user interface (GUI) and Sqlite3 for the database backend. Users can create an account and log in to access their task list. The tasks in a list are organized in the order they are created by default, with the option to sort by priority or due date. 

Overall, this application aims to simplify the task management process and help users become more organised and productive.


## Read the Docs
Documentation for the project has been generated using [pdoc](https://pdoc3.github.io/pdoc/)

and can be viewed [here](https://raw.githack.com/BradHillier/TaskMaster/main/docs/src.html) or by opening `./docs/src.html` 

Currently, not all files have documentation, though the following files are fully or partially documented:

### Fully Documented
* src.Model.TaskDAO
* src.Model.TaskListDAO
* src.View.SidebarView

### Partially Documented
* src.Model.TaskMaster
* src.Model.TaskList
* src.View.TaskScrollerView
* src.Controller.controller

The documentation also contains a use case diagram outlining the intended functionality of the program as well as an entity relationship diagram describing the database

## Installation
To download the repository first run

```bash
git clone https://github.com/BradHillier/TaskMaster
``` 

Once the repo has been cloned, use `cd TaskMaster` to enter the newly created taskmaster directory. From here, the entirety of the required setup can be handled by running

```bash
source setup.sh
``` 

Doing so will create a virtual environment in a directory called `venv`, activate the virtual environment and install all required dependencies. Additionally this script will create the sqlite3 database and populate it with test data.

After the script has finished running, you can start the program by running

```bash
./runner.py
``` 

which will use the instance of python3.9 located in the `venv/bin/` directory

### ⚠ Warning
If `setup.sh` is run without using `source`, all the dependencies will be installed outside of the virtual environment


## Usage

### Logging into TaskMaster

In it's current state, the login credentials are hard coded and registering new accounts has not been implemented. To access the app, input the following

**username:** test_user     
**password:** 123   

The below account also exists, but it has only a single empty list 
**username:** admin     
**password:** password    

## Support
For help running the application or troubleshooting issues, please send an email to [waking_clocks_0r@icloud.com](mailto:waking_clocks_0r@icloud.com)

## Authors and acknowledgment
This project was created as part of **CSCI 331 - Object Oriented Programming** at Vancouver Island University by:

**B**randon Cosh      
**R**ishabh Sharma     
**B**rad Hillier     


## Project status
There are still several features that have no been implemented including:

* registering new accounts
* creating new task lists

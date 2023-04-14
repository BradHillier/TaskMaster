#!/bin/bash

# the version of python on the cubs is python 3.9
# the below command ensures the correct version of 
# python is used when creating a virtual environment
if [ ! -d "venv" ]; then
    echo "creating virtual environment"
    python3.9 -m venv venv

else
    echo "virtual environment already exists"
fi
echo "activating virtual environment"

source venv/bin/activate
echo "installing required libraries"
# install all necessary libraries
pip3 install -r requirements.txt

echo "-------------------"
echo "setting up database"
echo "-------------------"
echo "Populating the users table"
sqlite3 database.sqlite3 '.read ./schema/users.sql'
echo "Populating the task lists table"
sqlite3 database.sqlite3 '.read ./schema/task_lists.sql'
echo "Populating the tasks table"
sqlite3 database.sqlite3 '.read ./schema/tasks.sql'
echo "database setup complete"

echo "Setup Complete! you can now run the program using './runner.py'"

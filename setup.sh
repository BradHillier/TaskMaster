#!/bin/bash

# the version of python on the cubs is python 3.9
# the below command ensures the correct version of 
# python is used when creating a virtual environment
if [ ! -d "venv" ]; then

    echo "creating virtual environment"
    python3.9 -m venv venv

    # install all necessary libraries
    pip3 install -r requirements.txt
else
    echo "virtual environment already exists"
fi

echo "setting up database"
sqlite3 database.sqlite3 '.read ./schema/users.sql'
sqlite3 database.sqlite3 '.read ./schema/task_lists.sql'
sqlite3 database.sqlite3 '.read ./schema/tasks.sql'



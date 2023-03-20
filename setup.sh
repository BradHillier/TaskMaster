#!/bin/bash

# the version of python on the cubs is python 3.9
# the below command ensures the correct version of 
# python is used when creating a virtual environment
python3.9 -m venv .

# install all necessary libraries
pip3 install -r requirements.txt

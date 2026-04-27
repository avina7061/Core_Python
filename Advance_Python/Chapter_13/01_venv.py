"""
if you install any package that installed globally so if you need of any other version of package
inside your any project so when you install pip install pandas==1.5.2 it unInstall previous existing package
globally

A virtual environment in Python is an isolated environment that contains its own Python interpreter and installed
packages,separate from the system (global) Python, allowing different projects to use different dependencies
without conflict.

# Step 1: Install virtualenv
pip install virtualenv

# Step 2: Create virtual environment
virtualenv env

# Step 3: Activate (PowerShell)
.\env\Scripts\Activate.ps1

# Step 4: Install required packages
pip install pandas
pip install flask

# Step 5: Deactivate environment
deactivate


# pip freeze is used to check all installed dependencies on your package

# for check you are in global system enviornment or virtual enviornment you see in terminal it written as (env)

#we simply output the all packages that shown by pi freeze into the requirement.txt file as:-
pip freeze > requirement.txt

if you have requirement.txt file you install directly all the packages that present in the requirement.txt as
pip install -r requirement.txt

"""
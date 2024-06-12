# Save this at any location in your computer, I tend to save it in my user/projects directory,
# this way I can run multiple projects from the same bash script if needed and install all the requirements
# in a single environment.

echo "--------------------------- Creating virtual environment ----------------------"
pip install --upgrade pip
pip install virtualenv
virtualenv venv
source ./venv/Scripts/active

echo "----------------------- Installing dependencies ------------------------------"
pip install -r {path_to_project_root}/requirements.txt

echo "----------------------- Running fileManager Script server -------------------------"
python {path_to_project_root}/src/main.py

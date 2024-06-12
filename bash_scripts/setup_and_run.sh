# Save this at any location in your computer, I tend to save it in my user/projects directory,
# this way I can run multiple projects from the same bash script if needed and install all the requirements
# in a single environment.

echo "--------------------------- Creating virtual environment ----------------------"
python3 -m pip install --upgrade pip
python3 -m pip install virtualenv
virtualenv venv
source {path_to_projects_dir}/venv/bin/activate

echo "----------------------- Installing dependencies ------------------------------"
python3 -m pip install -r {path_to_project_root}/requirements.txt

echo "----------------------- Running fileManager Script server -------------------------"
python3 {path_to_project_root}/src/main.py
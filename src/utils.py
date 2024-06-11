import os
from dotenv import load_dotenv
import shutil

load_dotenv()
DOWNLOADS_DIR = os.getenv('DOWNLOADS_DIR')


# Create directories based on the given object.
# Object values are arrays of subdirectories, keys are parent directory
def create_directories(dirs: dict, location: str):
    # Loop through the keys in the DIRS object and create a directory if it doesn't exist
    # and create the subdirectories.
    for key, value in dirs.items():
        os.makedirs(location + key, exist_ok=True)
        for i in value:
            os.makedirs(location + f'{str(key)}/{i}', exist_ok=True)
    print('Directories have been created successfully!')


# Reorganise downloads dir, sorting files into relevant subdirectories and sub-subdirectories by file extension
def reorganize_downloads():
    target_dirs = {
        'Downloaded Videos': ['.mov', '.mkv', '.mp4', '.avi', '.wmv'],
        'Downloaded Pictures': ['.jpg', '.jpg', '.png', '.gif', '.svg', '.webp', '.psd'],
        'Downloaded Documents': ['.pdf', '.doc', '.docx', '.csv', '.ppt',
                           '.zip', '.odt', '.xls', '.xlsx', '.ipynb',
                           '.xml', '.html', '.txt'],
        'Downloaded Installers': ['.dmg']
    }

    for key, value in target_dirs.items():
        reorganise_dir(DOWNLOADS_DIR, DOWNLOADS_DIR + key, value)
    print('Reorganised files successfully!')


def reorganise_dir(base_dir, target_dir_parent, file_extensions):
    for filename in os.listdir(base_dir):
        filepath = os.path.join(base_dir, filename)

        if os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in file_extensions):
            file_ext = filepath.split('.')[-1].lower()
            ext_dir = os.path.join(target_dir_parent, file_ext.upper() + 's')
            os.makedirs(ext_dir, exist_ok=True)
            # Move the file to the subdirectory
            shutil.move(filepath, os.path.join(ext_dir, filename))

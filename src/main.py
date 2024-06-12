"""
    Main python file where the code will be executed
"""
import json
import os
import subprocess
import sys
import importlib.resources as ilr
from utils import create_directories, reorganize_downloads
from dotenv import load_dotenv


# Main function, when called, starts the program.
def main():

    load_dotenv()
    with open('/Users/jonty/projects/fileManager/src/data/Download_DIRS.json', 'r') as DIRS:
        dirs = json.load(DIRS)
        location = os.getenv('DOWNLOADS_DIR')
        create_directories(dirs, location)
        reorganize_downloads()


if __name__ == "__main__":
    main()

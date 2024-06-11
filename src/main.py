"""
    Main python file where the code will be executed
"""
import os
from dotenv import load_dotenv
import json
from utils import create_directories, reorganize_downloads


# Main function, when called, starts the program.
def main():
    load_dotenv()
    with open('data/Download_DIRS.json', 'r') as DIRS:
        dirs = json.load(DIRS)
        location = os.getenv('DOWNLOADS_DIR')
        create_directories(dirs, location)
        reorganize_downloads()


if __name__ == "__main__":
    main()

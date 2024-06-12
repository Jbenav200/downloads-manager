# Downloads Folder Manager

This applications purpose is to organise files in the downloads folder specified in a .env file into subfolders
based on file category and file extension.

## Setup instructions
Once you've downloaded this repository, you will need to set up your own .env at the top level of the repo.

You'll need at least python3.10 for to run this locally. To check your python version you can run the following in your terminal:

```python3 --version```

You will want to run the following in your terminal before
executing ```python3 src/main.py```:

```python3 -m pip install -r requirements.txt```

This will ensure you have the python-dotenv package which will allow the program to read from the .env file you create 
at the top level of the repository.

## Run as an automation on MacOS
To run this script automatically you'll need to do a couple of things and
write a couple of files. Fortunately for you I've created boilerplate files for each.

The first thing you'll want to do is write a [bash script](bash_scripts/setup_and_run.sh) to create/activate a virtual environment to run python, 
install the requirements and execute the main.py script.

The second thing you'll want to do is write create a cron job that executed the bash script and logs to a file in the
same location.

I recommend saving the bash script in a projects directory under your user, where you can save all of your projects.
This is where I usually save any of my projects, including this one.

To create your cron job on MacOS you want to execute the following command in the terminal:

```crontab -e```

You may be asked to select an editor (vim/nano). I prefer to use nano, but it's really up to you.
Edit the path in curly brackets in the [file provided](bash_scripts/crontab) and copy and paste it into your local 
crontab file.

Now you have set up the cron job and the script automation should run every minute. You can read more about 
cron jobs [here
](https://www.doabledanny.com/cron-jobs-on-mac).
### Categories
- Downloaded Pictures
- Downloaded Videos
- Downloaded Documents
- Downloaded Installers

### File Extensions supported
- Pictures
  - JPG
  - PNG
  - SVG
  - WEBP
  - PSD
- Videos
  - MKV
  - MOV
  - MP4
  - AVI
  - WMV
- Documents
  - DOC
  - DOCX
  - PDF
  - PPT
  - XLS
  - XLSX
  - IPYNB
  - HTML
  - TXT
  - XML
  - ZIP
  - ODT
  - CSV
- Installers
  - DMG
# Downloads Folder Manager

This applications purpose is to organise files in the downloads folder specified in a .env file into subfolders
based on file category and file extension.

## Setup instructions
Once you've downloaded this repository, you will need to set up your own .env at the top level of the repo.

You'll need at least python3.10 for to run this locally. To check your python version you can run the following in your terminal:

```python3 --version```

You will want to run the following in your terminal before
executing ```python3 main.py```:

```python3 -m pip install -r requirements.txt```

This will ensure you have the python-dotenv package which will allow the program to read from the .env file you create 
at the top level of the repository.


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
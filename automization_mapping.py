import subprocess
from tkinter import filedialog
from tkinter import *

# list of mapping files
list = ["ActiveIngredients", "Agent", "ApplicationRate", "BufferConstraints", "Constraints", "Crop", "CropLang", "Indication", "Pest", "PestLang", "Time"]

# create small GUI for selecting the SQLite DB
root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("SQLite", "*.sqlite")))
path = root.filename

# change path in mapping files and start rmlmapper
for item in list:
    with open('PATHTOMAPPINGFILE'+item+'.ttl','r',encoding='utf-8') as f:
        text = f.read()
        newtext = text.replace("path", path)
# create Tempfile with Path to DB
        with open('PATHTOTEMPFILE','w',encoding='utf-8') as file:
            file.write(newtext)
            file.close()
            command = 'java -jar rmlmapper-VERSION-all.jar -m PATHTOTEMPFILE -o PATHTORESULTFILE'+item+'.ttl -s turtle'
            p = subprocess.call(command.split())
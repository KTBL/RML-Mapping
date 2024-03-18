# RML-Mapping
This repository contains Mappingfiles for [rmlmapper-java](https://github.com/RMLio/rmlmapper-java)

Note: SQLite and Access DB Sources are not supported by rmlmapper-java yet. However, find a forked and adapted version inside the [KTBL Repository](https://github.com/KTBL/rmlmapper-java)

## DB Source 

Adapt Path of Source and JDBC Driver of DB

```
<#DB_source> a d2rq:Database;
    d2rq:jdbcDSN "jdbc:sqlite:path";
    d2rq:jdbcDriver "org.sqlite.JDBC";
    d2rq:username "";
    d2rq:password "".
```

## Run rmlmapper-java

run inside "target" folder or with path to target folder of rmlmapper-java:

```java -jar rmlmapper-VERSION-all.jar -m Path\Mappingfile.ttl -o Path\Resultfile.ttl -s format```


You can run one or more mappingfiles, however the mapping will only fill one result file. If no resultfile is given, it will be written into the working directory.
Several formats are available. We use mostly turtle.

## Path Adaption in several files
This is a short script written in python to insert the DB path into the placeholder and to map several files sequentially.
If only one mapping file should be mapped, remove the unneccessary strings from the list.

```
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
```        





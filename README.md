# RML-Mapping
This repository contains Mappingfiles for [rmlmapper-java](https://github.com/RMLio/rmlmapper-java)

Note: SQLite and Access DB Sources are not supported by rmlmapper-java yet. However, find a forked and adapted version inside the [KTBL Repository](https://github.com/KTBL/rmlmapper-java)

## DB Source 

Adapt Path of Source and JDBC Driver of DB

```
<#DB_source> a d2rq:Database;
    d2rq:jdbcDSN "jdbc:sqlite:PathToDB";
    d2rq:jdbcDriver "org.sqlite.JDBC";
    d2rq:username "";
    d2rq:password "".
```

## Run rmlmapper-java

run inside "target" folder or with path to target folder of rmlmapper-java:

``java -jar rmlmapper-VERSION-all.jar -m Path\Mappingfile.ttl -o Path\Resultfile.ttl -s format``

You can run one or more mappingfiles, however the mapping will only fill one result file. If no resultfile is given, it will be written into the working directory.
Several formats are available. We use mostly turtle.

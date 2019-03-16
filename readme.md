Convex Take Home Assignment\
Ben Warfield\
bwarfield1@gmail.com


General:\
I created a virtual environment to control for dependencies which can be found in requirements.txt.  Please install all dependencies.  This pipeline will require a SQL server connection and uploading capability will not work until the SQL server is up and login credentials are entered in db.py.

To take a look at the data without uploading, run main.py lines 1-9.

**abnb_data.py** ingests the .csv data and grabs pertinent columns.\
**db.py** handles our database connection\
**main.py** would be our file for executing the data pipeline\
**models.py** defines our python definition of database model\
**pipe.py** merges the data and brings it all together in a data frame.
Convex Take Home Assignment
Ben Warfield
bwarfield1@gmail.com


General:
I created a virtual environment to control for dependencies which can be found in requirements.txt.  Please install all dependencies.  This pipeline depends on the creation of a SQL server.  This pipeline will not work until the SQL server is up and login credentials are entered in db.py.

**abnb_data.py** ingests the .csv data and grabs pertinent columns.
**db.py** handles our database connection
**main.py** would be our file for executing the data pipeline
**models.py** defines our python definition of database model
**pipe.py** merges the data and brings it all together in a data frame.
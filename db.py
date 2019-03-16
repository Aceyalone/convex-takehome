"""
Hypothetical database session and global configuration
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# Database creation needed for db operations.  We would need to stand up a SQL
# server and fill out username and password for this to work.
usn = 'username'
pwd = 'password'
engine = create_engine("mssql+pyodbc://{}:{}@address.of.sql.server:port/".format(usn, pwd))
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

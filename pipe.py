"""
INSIDE AIRBNB DATA PIPELINE - SF

This module handles the building of the data pipe from Inside AirBnB's
San Francisco csv files as well as uploading it to our non-existent SQL
database.
"""

import abnb_data as abnb
import json
from models import sf_abnb_data
#from db import engine, session


def build():
	# This function builds the data pipe and can be used to perform
	# any required data cleansing or transformations. I just do a 
	# join here to bring the summary data and detailed data together.
	base_data = abnb.get_list_summary()
	base_data = base_data.merge(abnb.get_list_details(), how='left', on='id')
	return base_data

def upload(data):
	# This function handles the ingestion of the data into a hypothetical SQL
	# database which can be queried by data scientists or integrated into a 
	# company API.  It first checks whether an update is required by querying
	# the last_scraped field in our database and checking against what's 
	# available through Inside AirBnB.  I currently have it set up so that 
	# once new data is availabile it will just add the new data as new rows
	# and not overwrite the old rows.  If database size were to become a 
	# concern I would implement some upsert or truncating logic.
    last_updated = engine.execute("SELECT DISTINCT last_scraped " \
    	                          "FROM sf_abnb_table").fetchall()
    if data['last_scraped'][0] == last_updated:
        print('No updates to SF AirBnB data')
    else:
        print('Updates to SF AirBnB data found.  Updating...')
        json_records = json.loads(data.to_json(orient='records', date_format='iso'))
        session.bulk_insert_mappings(sf_abnb_data, json_records, render_nulls=True)
        session.commit()

def run():
	# Run command to streamline the data pipe and uploading processes
    upload(build())
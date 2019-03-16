"""
INSIDE AIRBNB DATA READER

Module to handle the reading of .csv and .gzip data from Inside AirBnB 
"""

import pandas as pd


def get_list_details():
    # This will grab the listing detail dataset from Inside AirBnB
    # and return it in a pandas dataframe.  It will also drop
    # un-wanted columns.
    sf_detail_url = 'http://data.insideairbnb.com/united-states/ca/'\
        'san-francisco/2019-03-06/data/listings.csv.gz'
    dat = pd.read_csv(sf_detail_url, compression='gzip')
    keep = ['id','host_response_time','host_is_superhost','accommodates',\
        'bathrooms','bedrooms','beds','square_feet','cancellation_policy',\
        'review_scores_rating','last_scraped']
    return dat[keep]

def get_list_summary():
    # This will grab the listing summary data and return it in a pandas
    # dataframe.
    sf_url = 'http://data.insideairbnb.com/united-states/ca/san-francisco/'\
        '2019-03-06/visualisations/listings.csv'
    return pd.read_csv(sf_url)


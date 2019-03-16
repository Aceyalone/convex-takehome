import pandas as pd

def get_list_details():
    sf_detail_url = 'http://data.insideairbnb.com/united-states/ca/'\
        'san-francisco/2019-03-06/data/listings.csv.gz'
    dat = pd.read_csv(sf_detail_url, compression='gzip')
    keep = ['id','host_response_time','host_is_superhost','accommodates',\
        'bathrooms','bedrooms','beds','square_feet','cancellation_policy',\
        'review_scores_rating']
    dat = dat[keep]
    return dat

def get_list_summary():
    sf_url = 'http://data.insideairbnb.com/united-states/ca/san-francisco/2019'\
        '-03-06/visualisations/listings.csv'
    return pd.read_csv(sf_url)


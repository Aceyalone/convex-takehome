"""
Principal python definition of database model.  For now it's just our
SF Listing data from Inside AirBnB.
"""

from sqlalchemy import Column, Integer, String, DateTime, Numeric                   
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class sf_abnb_data(Base):
    __tablename__ = "sf_abnb_table"
    id = Column(Integer, primary_key = True, nullable = False)
    name = Column(String(50), nullable = True)
    host_id = Column(Integer, nullable=True)
    host_name = Column(String(50), nullable = True)
    neighbourhood_group = Column(String(50), nullable = True)
    neighbourhood = Column(String(50), nullable = True)
    latitude = Column(Numeric, nullable = True)
    longitude = Column(Numeric, nullable = True)
    room_type = Column(String(25), nullable = True)
    price = Column(Numeric, nullable = True)
    minimum_nights = Column(Integer, nullable = True)
    number_of_reviews = Column(Integer, nullable = True)
    last_review = Column(DateTime(timezone = True), nullable = True)
    reviews_per_month = Column(Numeric, nullable = True)
    calculated_host_listings_count = Column(Numeric, nullable = True)
    availability_365 = Column(Numeric, nullable = True)
    host_response_time = Column(Numeric, nullable = True)
    host_is_superhost = Column(String(10), nullable = True)
    accommodates = Column(Numeric, nullable = True)
    bathrooms = Column(Numeric, nullable = True)
    bedrooms = Column(Numeric, nullable = True)
    beds = Column(Numeric, nullable = True)
    square_feet = Column(Numeric, nullable = True)
    cancellation_policy = Column(String(50), nullable = True)
    review_scores_rating = Column(Numeric, nullable = True)
    last_scraped = Column(DateTime(timezone = True), nullable = True)
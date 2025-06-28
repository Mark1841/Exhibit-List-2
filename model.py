from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Define exhibit class
class Exhibit(Base):
    """ This class creates the Exhibit data model and links to database table """
    __tablename__ = "exhibits"
    id = Column(Integer, primary_key=True)
    exhibit_number = Column(Integer, unique=True)
    placard_number = Column(Integer)
    property_tag = Column(String, unique=True)
    cfs_number = Column(String)
    photograph_number = Column(String)
    description = Column(String)
    location = Column(String)
    results = Column(String)
    seized_from = Column(String)
    seized_by = Column(String)
    seized_date_time = Column(String)
    seal_number = Column(String)
    seal_date_time = Column(String)

# Define continuity class
class Continuity(Base):
    """ This class creates the continuity data model and links to the continuity table """
    pass # Code to go here to define the continuity table and link to exhibit table

# Database set up
engine = create_engine('sqlite:///exhibitList.db', echo = False)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

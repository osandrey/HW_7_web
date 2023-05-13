from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('postgresql://postgres:1111@localhost/hw_7_web')
Base = declarative_base()
DBSession = sessionmaker(bind=engine)
session = DBSession()

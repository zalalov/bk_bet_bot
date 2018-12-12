from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from config import get_config

config = get_config()

Base = declarative_base()

engine = create_engine(config.DB_CONNECTION_STRING, echo=True)
Session = sessionmaker(bind=engine)

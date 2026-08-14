import os  #built in module to interact with OS                                                                                                                

from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv() # Loads variable from .env

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) # creates the SQLALchemy Engine, which manages communication with PostgreSQL


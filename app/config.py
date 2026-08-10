import os
from dotenv import load_dotenv

load_dotenv() # loads the variable from .env

APP_NAME = os.getenv("APP_NAME")
APP_VERSION = os.getenv("APP_VERSION")
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_NAME = os.environ.get('DATABASE_NAME')
USERNAME = os.environ.get('USERNAME')
PASSWORD = os.environ.get('PASSWORD')
HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')

import os
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

#Get creds from the environment or pull defaults
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'password')
POSTGRES_URI = os.environ.get('POSTGRES_URI', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')

#Build the connection string
DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_URI}/{POSTGRES_DB}"
engine = create_engine(DATABASE_URL)

app = FastAPI()

@app.get("/")
def read_root():
    return "I'm alive"

@app.get("/db")
def get_db():
    version = pd.read_sql("SELECT version()", engine)
    clean_version = ' '.join(version['version'][0].split(' ')[0:2])

    return clean_version
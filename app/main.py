import os
from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd

#Get creds from the environment or pull defaults
DB_USER = os.environ.get('DB_USER', 'postgres')
DB_PASSWORD = os.environ.get('DB_PASSWORD', 'password')
DB_URI = os.environ.get('DB_URI', 'localhost')
DB_NAME = os.environ.get('DB_NAME', 'postgres')

#Build the connection string
DATABASE_URL = f"postgres://{DB_USER}:{DB_PASSWORD}@{DB_URI}/{DB_NAME}"
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
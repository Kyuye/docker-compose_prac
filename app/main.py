
from typing import Optional
from fastapi import FastAPI

import sqlalchemy as db
import logging
import os


engine = db.create_engine('mysql+pymysql://root:1234@mysql-db/bunnyburrow')

connection = engine.connect()

metadata = db.MetaData()

table = db.Table('friends', metadata, autoload=True, autoload_with=engine) 
query = db.select([table])
result_proxy = connection.execute(query)
result_set = result_proxy.fetchall()

data = {}
for r in result_set:
    name, addr = r
    data[name] = addr

app = FastAPI()

@app.get("/")
def read_root():
    return data


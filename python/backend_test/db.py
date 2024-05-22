import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, MetaData, Table, create_engine
from databases import Database

load_dotenv()
host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
dbname = os.getenv("DB_DBNAME")
db_default = os.getenv("DB_DEFAULT")

DATABASE_URL = "postgresql://"+user+":"+password+"@"+host+"/"+dbname

engine = create_engine(DATABASE_URL)
metadata = MetaData()

quotes = Table(
    "quotestable",
    metadata,
    Column("id",Integer, primary_key=True, index=True),
    Column("quotetext",String),
    Column("quotesource",String)
)

database = Database(DATABASE_URL)
from fastapi import FastAPI
from contextlib import asynccontextmanager

from db import engine, metadata, database
from api import quotes

metadata.create_all(engine)



@asynccontextmanager
async def db(app: FastAPI):
    try:
        print("Starting up...")
        await database.connect()
        yield
    finally:
        print("Shutting down...")
        await database.disconnect()

app = FastAPI(lifespan=db)

app.include_router(quotes.router)

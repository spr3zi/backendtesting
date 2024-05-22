import random
from sqlalchemy import text
from api.models import QuoteSchema
from db import quotes, database

async def get_random_quote():
    total = await database.execute(text("SELECT reltuples AS estimate FROM pg_class where relname = 'quotestable';"))
    query = quotes.select().where(quotes.c.id == random.randint(1,int(total)))
    quote = await database.fetch_one(query)
    return quote

async def get_first_quote():
    query = quotes.select().where(quotes.c.id == 1)
    quote = await database.fetch_one(query)
    return quote
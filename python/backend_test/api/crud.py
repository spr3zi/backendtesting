import random
from sqlalchemy import text
from api.models import QuoteSchema
from db import quotes, database

async def get_random_quote():
    #total = await database.execute(text("SELECT reltuples AS estimate FROM pg_class where relname = 'quotestable';"))
    total = await database.execute(text("SELECT COUNT(*) FROM quotestable;"))
    query = quotes.select().where(quotes.c.id == random.randint(1,int(total)))
    quote = await database.fetch_one(query)
    return quote

async def get_quote(quote_id):
    query = quotes.select().where(quotes.c.id == quote_id)
    quote = await database.fetch_one(query)
    return quote

async def post(payload: QuoteSchema):
    query  = quotes.insert().values(quotesource=payload.quotesource,
                                    quotetext=payload.quotetext)
    return await database.execute(query)
    

async def delete(quote_id):
    query = quotes.delete().where(quotes.c.id == quote_id)
    return await database.execute(query)

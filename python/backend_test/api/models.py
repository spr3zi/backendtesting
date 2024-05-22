from pydantic import BaseModel, Field

class QuoteSchema(BaseModel):
    quotesource: str
    quotetext: str

class QuoteDB(QuoteSchema):
    id: int
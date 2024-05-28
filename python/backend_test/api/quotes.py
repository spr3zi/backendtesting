import api.crud as crud
from api.models import QuoteSchema, QuoteDB
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()

@router.get("/")
async def get_random_quote():
    quote = await crud.get_random_quote()
    if not quote:
        raise HTTPException(status_code=404, detail="Error retrieving random quote")
    return quote

@router.get("/{quote_id}")
async def get_quote(quote_id: int):
    quote = await crud.get_quote(quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Error retrieving quote")
    return quote

@router.post("/", response_model=QuoteDB)
async def create_quote(payload: QuoteSchema):
    quote_id = await crud.post(payload)
    response_object = {
        "id": quote_id,
        "quotesource": payload.quotesource,
        "quotetext": payload.quotetext
    }
    return response_object

@router.delete("/{quote_id}/")
async def delete_quote(quote_id: int):
    quote = await crud.get_quote(quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found.")
    await crud.delete(quote_id)
    return quote
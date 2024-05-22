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


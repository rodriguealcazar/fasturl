from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    price_with_tax: Optional[float] = None


app = FastAPI()


@app.get("/")
async def root():
    return {
        "message": "Hello world."
    }


@app.get("/items/default")
async def read_item():
    return {
        "item_id": "default item."
    }


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {
        "item_id": item_id
    }


@app.post("/items/")
async def create_item(item: Item):
    if item.tax:
        item.price_with_tax = item.price + item.tax
    return item

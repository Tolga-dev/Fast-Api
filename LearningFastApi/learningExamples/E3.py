from typing import Any

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()
fake_db = {}

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []

class OutPutItem(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float

class BaseUser(BaseModel):
    username: str
    email: str
    full_name: str | None = None

class UserIn(BaseUser):
    password: str

@app.post("/user/")
async def create_user(user: UserIn) -> BaseUser:
    return user


@app.post("/items/")
async def create_item(item: Item) -> Item:
    return item


@app.get("/items/", response_model=list[Item])
async def read_items() -> Any:
    return [
        Item(name=" Gun", price=42.0),
        Item(name="Plumbus", price=32.0),
    ]

@app.post("/items-output/", response_model=OutPutItem)
async def read_item_outputs(item: Item) -> Any:
    return item


@app.put("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data

if __name__ == "__main__":
    uvicorn.run("E3:app", host="127.0.0.1", port=8000, reload=True)
    
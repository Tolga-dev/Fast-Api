from email.header import Header
from enum import Enum
from typing import Optional, Annotated

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

fake_items_db = [{1: "Foo"}, {2: "Bar"}, {3: "Baz"}]
app = FastAPI()
    

class ModelName(str, Enum):
    a = "1"
    b = "2"
    c = "3"
    
class Item(BaseModel):
    name : str
    price: float
    tax: Optional[float] = 0

class BookCreateModel(Item):
    pass


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    item.name = "Renewed " + item.name
    return {"item_id": item_id, **item.model_dump()}

@app.post("/items-body")
async def create_item(body: Item):
    tax = body.tax
    return tax + body.price

@app.post("/create_book")
async def create_book(book_data: BookCreateModel):
    return {
        "title": book_data.name,
        "price": book_data.price,
    }

@app.get("/get_headers")
async def get_header(
        accept: Annotated[str | None, Header()] = None,
        content_type: Annotated[str | None, Header()] = None,
        user_agent: Annotated[str | None, Header()] = None):
    
    return {"Accept": accept, 
            "Content-Type": content_type, 
            "User-Agent": user_agent}
    
            
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id : int):
    return {"item_id": fake_items_db[item_id]} 

@app.get("/names/{name}")
async def read_name(name):
    return {"name": name}

@app.get("/models/{model_name}")
async def read_model(model_name: ModelName):
    return {"model_name": model_name, "message":"Hello World sadsd"}

@app.get("/users")
async def read_users():
    return ["Tolga", "Konat"]

@app.get("/cars/{car_model_name}")
async def read_model(model_name):
    return {"model_name": model_name, "message":"Hello World sadsd"}

@app.get("/files/{filepath:path}")
async def read_file(filepath : str):
    return {"filepath": filepath}

@app.get("/items/")
async def read_items():
    return fake_items_db

if __name__ == "__main__":
    uvicorn.run("E1:app", host="127.0.0.1", port=8000, reload=True)
    
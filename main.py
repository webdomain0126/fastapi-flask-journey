from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Day 4 FastAPI", version="0.1.0")

# 1) Root endpoint
@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI Day 4!"}

# 2) Path parameter
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "note": "Path parameter works"}

# 3) Query parameter
@app.get("/search")
def search_items(q: Optional[str] = None, limit: int = 10):
    return {"query": q, "limit": limit}

# 4) Request body with Pydantic
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True
    description: Optional[str] = None

@app.post("/items")
def create_item(item: Item):
    return {"created": item}

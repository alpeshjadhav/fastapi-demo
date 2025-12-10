from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool = True

items = {}

@app.post("/items")
def create_item(item: Item):
    items[item.name] = item
    return item

@app.get("/items")
def read_all_items():
    return list(items.values())

@app.get("/items/{name}")
def read_item(name: str):
    return items.get(name, {"error": "Item not found"})

@app.put("/items/{name}")
def update_item(name: str, item: Item):
    items[name] = item
    return item

@app.delete("/items/{name}")
def delete_item(name: str):
    return items.pop(name, {"error": "Item not found"})

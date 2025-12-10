from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="iPhone 15", description="Apple flagship smartphone", price=999, quantity=20),
    Product(id=2, name="Samsung Galaxy S23", description="Samsung premium smartphone", price=899, quantity=15),
    Product(id=3, name="OnePlus 11", description="Fast performance Android smartphone", price=699, quantity=18),
    Product(id=4, name="Google Pixel 8", description="Google AI-powered smartphone", price=799, quantity=12),
    Product(id=5, name="Xiaomi 13 Pro", description="High-end camera phone by Xiaomi", price=650, quantity=25),
    Product(id=6, name="Realme GT 3", description="Performance phone with fast charging", price=550, quantity=30),
    Product(id=7, name="Vivo X90", description="Flagship camera phone by Vivo", price=720, quantity=14),
    Product(id=8, name="Oppo Find X6", description="Premium smartphone with great display", price=780, quantity=10),
    Product(id=9, name="Motorola Edge 40", description="Lightweight and stylish smartphone", price=500, quantity=22),
    Product(id=10, name="Nothing Phone 2", description="Unique transparent smartphone", price=599, quantity=16),
]


@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}

@app.get("/products")
def get_all_products():
    return products

@app.get("/products/{id}")
def get_all_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return {"message": "Product updated successfully"}
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return {"message": "Product deleted successfully"}
    return {"error": "Product not found"}
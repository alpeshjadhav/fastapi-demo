from fastapi import FastAPI, HTTPException
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

# Get all products
@app.get("/products")
def get_all_products():
    return products

# Get product by ID
@app.get("/products/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

# Add new product
@app.post("/products")
def add_product(product: Product):
    # prevent duplicate IDs
    for p in products:
        if p.id == product.id:
            raise HTTPException(status_code=400, detail="Product with this ID already exists")

    products.append(product)
    return product

# Update product
@app.put("/products/{id}")
def update_product(id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == id:
            # keep ID same even if user changes in body
            updated_product.id = id
            products[index] = updated_product
            return {"message": "Product updated successfully"}

    raise HTTPException(status_code=404, detail="Product not found")

# Delete product
@app.delete("/products/{id}")
def delete_product(id: int):
    for index, product in enumerate(products):
        if product.id == id:
            del products[index]
            return {"message": "Product deleted successfully"}

    raise HTTPException(status_code=404, detail="Product not found")

# from fastapi import FastAPI
# from product import products

# app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Hello World"}

# @app.get("/products")
# def get_products():
#     return products
from fastapi import FastAPI

from app.products import products

@app.get("/products")
def get_products():
    return products
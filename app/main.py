from fastapi import FastAPI
from pro import products

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello World"}



@app.get("/contect")
def home():
    return products

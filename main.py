from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn

app = FastAPI()

data = [
    {
        "name": "Samsung 103in Curved TV",
        "description": "Its supa curvy and thiccc",
        "price": 999.99,
        "id": "2342342332"
    },
    {
        "name": "Samsung 99in TV",
        "description": "Its supa thiccc",
        "price": 700,
        "id": "12312"
    },
    {
        "name": "Sony 27in Monitor",
        "description": "Really good crispy monitor",
        "price": 100.22,
        "id": "123sdf"
    }
]


class Product(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    id: str

@app.get("/")
async def root():
    return {"message": "Hello the api is working very nice"}


@app.get("/products/")
async def get_all_products(size: int = 0):
    if size == 0:
        return data
    else:
        return data[:size]



@app.get("/products/{product_id}")
async def get_all_products(product_id: str):
    for x in data:
        print(x['id'])
        if x['id'] == str(product_id):
            return x
    return str("The product you were looking for with id "+ product_id + " was not in our system")


@app.post("/products/create")
async def create_some_product(my_product: Product):
    data.append(my_product)
    return data


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
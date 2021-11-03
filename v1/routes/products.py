from fastapi import APIRouter
from core.schemas import product

Product = product.Product
router = APIRouter()

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

@router.get("/")
async def get_all_products(size: int = 0):
    if size == 0:
        return data
    else:
        return data[:size]



@router.get("/{product_id}")
async def get_all_products(product_id: str):
    for x in data:
        print(x['id'])
        if x['id'] == str(product_id):
            return x
    return str("The product you were looking for with id "+ product_id + " was not in our system")


@router.post("/create")
async def create_some_product(my_product: Product):
    data.append(my_product)
    return data

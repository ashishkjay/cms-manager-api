from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI
import uvicorn
from v1.routes import health, products
app = FastAPI()

app.include_router(health.router)
app.include_router(
    products.router,
    prefix="/products",
    tags=["products"],
    responses={418: {"description": "I'm a teapot"}, 200: {"description": "OK"}},
)

@app.get("/")
async def root():
    return {"message": "Hello the api is working very nice"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
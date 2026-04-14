from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DiscountRequest(BaseModel):
    price: float
    discount_percent: float

@app.post("/calculate_discount")
def calculate_discount(request: DiscountRequest):
    final_price = request.price - (request.price * request.discount_percent/100)
    return {"final_price": final_price}
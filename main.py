import hashlib
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

def bad_style():
  x=1
  y=2
  return x

@app.get("/login")
def login():
    # Bandit will catch this weak MD5 hashing algorithm
    m = hashlib.md5()
    m.update(b"super_secret_password")
    return {"token": m.hexdigest()}
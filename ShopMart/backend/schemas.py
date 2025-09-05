
from pydantic import BaseModel

class ProductBase(BaseModel):
    name: str
    description: str
    price: float
    image: str

class ProductCreate(ProductBase): pass
class Product(ProductBase):
    id: int
    class Config: orm_mode = True

class UserCreate(BaseModel):
    username: str
    password: str

class User(BaseModel):
    id: int
    username: str
    class Config: orm_mode = True

class LoginRequest(BaseModel):
    username: str
    password: str

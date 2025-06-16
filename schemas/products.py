from pydantic import BaseModel

class Product(BaseModel):
    name : str
    price : int
    category_id : int
    photo : str
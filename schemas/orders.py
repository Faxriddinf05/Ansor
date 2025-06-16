from pydantic import BaseModel
from datetime import date


class OrderS(BaseModel):
    date : date
    product_id : int
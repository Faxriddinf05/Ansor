from sqlalchemy import Column, Integer, Date, ForeignKey
from db import Base

class OrderM(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
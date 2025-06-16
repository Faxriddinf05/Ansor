from sqlalchemy import Column, String, Integer, ForeignKey
from db import Base

class ProductM(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    price = Column(Integer, nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    photo = Column(String(255), nullable=True)

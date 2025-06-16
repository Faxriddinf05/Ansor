from sqlalchemy import Column, String, Integer
from db import Base

class CategoryM(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)


from db import Base
from sqlalchemy import Column, String, Integer


class UserM(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(20), nullable=False)
    image = Column(String(255), nullable=True)
    phone_number = Column(Integer, nullable=False)
from pydantic import BaseModel, Field, EmailStr

class UserSch(BaseModel):
    full_name: str
    password: str = Field(..., min_length=4, description="Parol kamida 4 ta belgidan iborat bo'lishi kerak!!!")
    email: EmailStr
    phone_number: int


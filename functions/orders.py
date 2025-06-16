from models.orders import OrderM
from schemas.orders import OrderS
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete


async def add_order(form:OrderM):
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, delete
from models.categories import CategoryM
from models.users import UserM
from schemas.categories import CategoryS
from db import database
from fastapi import HTTPException


async def add_category(form, db:AsyncSession, current_user : UserM):
    check_user = await db.execute(select(UserM).where(UserM.role == current_user.role))
    user_info = check_user.scalar()
    if user_info.role != "admin":
        raise HTTPException(403, "Sizga ruxsat yo'q !")


    check_category = await db.execute(select(CategoryM).where(CategoryM.name == form.name))
    category_exists = check_category.scalar()
    if category_exists:
        raise HTTPException(400, "Bunday tur avval qo'shilgan !")

    new_category = CategoryM(
        name = form.name
    )
    db.add(new_category)
    await db.commit()
    return "Yangi tur(bo'lim) qo'shildi"

async def change_category(ident:int, form, db:AsyncSession, current_user : UserM):
    check_user = await db.execute(select(UserM).where(UserM.role == current_user.role))
    user_info = check_user.scalar()
    if user_info.role != "admin":
        raise HTTPException(403, "Sizga ruxsat yo'q !")


    await db.execute(update(CategoryM).where(CategoryM.id == ident).values(
            name = form.name
        ))
    await db.commit()
    return "Tur tahrirlandi"


async def delete_category(ident, db:AsyncSession, current_user : UserM):
    check_user = await db.execute(select(UserM).where(UserM.role == current_user.role))
    user_info = check_user.scalar()
    if user_info.role != "admin":
        raise HTTPException(403, "Sizga ruxsat yo'q !")

    check_type = await db.execute(select(CategoryM).where(CategoryM.id == ident))
    type_exists = check_type.scalar()
    if not type_exists:
        raise HTTPException(400, "Bunday tur mavjud emas !")

    await db.execute(delete(CategoryM).where(CategoryM.id == ident))
    await db.commit()
    return "Tur o'chirildi !"

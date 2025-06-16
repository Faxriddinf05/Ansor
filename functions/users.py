from routers.login import get_password_hash
# from utils.db_operations import save_in_db
from models.users import UserM
from fastapi import HTTPException
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import update, delete
from utils.image import save_image





# # o'zini ko'rish funksiyasi
# async def get_own(db:AsyncSession, current_user):
#     result = await db.execute(select(UserM).where(UserM.email == current_user.email))
#     return result.scalars().first()
async def get_own(db: AsyncSession, current_user: UserM):
    result = await db.execute(select(UserM).where(UserM.email == current_user.email))
    user = result.scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="Foydalanuvchi topilmadi")
    return user






# foydalanuvchini qo'shish
async def sign_up(form, db:AsyncSession, current_user : UserM):          # add_user degani
    check_user = await db.execute(select(UserM).where(UserM.email == form.email))
    user_exists = check_user.scalar()
    if user_exists:
        raise HTTPException(400, "Bunday email avval ro'yhatga olingan !")


    new_user = UserM(
        full_name = form.full_name,
        password = get_password_hash(form.password),
        role = "user",
        email = form.email,
        phone_number = form.phone_number
    )
    db.add(new_user)
    await db.commit()
    return "Foydalanuvchi ro'yhatga olindi "


# admin qo'shish
async def add_admin(form, db:AsyncSession, current_user : UserM):
    check_user = await db.execute(select(UserM).where(UserM.role == current_user.role))
    user_info = check_user.scalar()
    if user_info.role != "admin":
        raise HTTPException(403, "Sizga ruxsat yo'q !")

    new_admin = UserM(
        full_name = form.full_name,
        role = "admin",
        password = get_password_hash(form.password),
        email = form.email,
        phone_number = form.phone_number
    )
    db.add(new_admin)
    await db.commit()
    return "Admin qo'shildi !"



# o'zini tahririlash
async def update_self(form, db:AsyncSession, current_user : UserM):

    await db.execute(update(UserM).where(UserM.email == current_user.email).values(
            full_name = form.full_name,
            role = "admin",
            password = get_password_hash(form.password),
            email = form.email,
            phone_number = form.phone_number
        ))
    await db.commit()
    return "Ma'lumotlaringiz tahrirlandi"





# o'ziga rasm yuklash
async def user_image(file, db: AsyncSession, current_user : UserM):

    image_filename = await save_image(file)

    async with db as session:
        result = await session.execute(select(UserM).filter(UserM.id == current_user.id))
        user = result.scalar()

        if not user:
            raise HTTPException(status_code=404, detail="User topilmadi")

        user.image = image_filename
        await session.commit()
        return "Rasm yuklandi !"





# o'zini o'chirib yuborish
async def delete_self(db : AsyncSession, current_user : UserM):
    check_user = await db.execute(select(UserM).where(UserM.email == current_user.email))
    user_exists = check_user.scalar()
    if not user_exists:
        raise HTTPException(400, "Bunday email mavjud emas !")

    await db.execute(delete(UserM).where(UserM.email == current_user.email))
    await db.commit()
    return "O'zingizni o'chirdingiz !"




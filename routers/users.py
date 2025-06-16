from functions.users import get_own, sign_up, add_admin, update_self, user_image, delete, delete_self
from fastapi import APIRouter, Depends, HTTPException, UploadFile
from models.users import UserM
from routers.login import get_current_user
from schemas.users import UserSch
from db import database
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


user_router = APIRouter()
admin_router = APIRouter()


@user_router.get('/get_own_lock')
async def ozini_korish(db: AsyncSession = Depends(database), current_user: UserM = Depends(get_current_user)):
    """
    Ro'yhatdan o'tgan foydalanuvchi o'zi haqidagi ma'lumotlarni ko'radi
    :param db:
    :param current_user:
    :return:
    """
    return await get_own(db, current_user)



@user_router.get('/get_users_lock')
async def foydalanuvchilarni_korish(db:AsyncSession=Depends(database), current_user: UserM = Depends(get_current_user)):
    result = await db.execute(select(UserM))
    try:
        return result.scalars().all()
    except Exception as h:
        raise (HTTPException(400, str(h)))



@user_router.post('/post_users')
async def foydalanuvchi_qoshish(form:UserSch, db:AsyncSession = Depends(database), current_user : UserM = Depends(get_current_user)):
    try:
        return await sign_up(form, db, current_user)
    except Exception as e:
        raise HTTPException(400, str(e))


@admin_router.post('/post_admin')
async def admin_qoshish(form:UserSch, db:AsyncSession = Depends(database), current_user : UserM = Depends(get_current_user)):
    try:
        return await add_admin(form, db, current_user)
    except Exception as f:
        raise HTTPException(400, str(f))



@user_router.put('/put_own')
async def ozini_tahrirlash(form:UserSch, db:AsyncSession = Depends(database), current_user : UserM = Depends(get_current_user)):
    try:
        return await update_self(form, db, current_user)
    except Exception as d:
        raise HTTPException(400, str(d))


@user_router.post('/load_image')
async def oziga_rasm_yuklash(file:UploadFile, db:AsyncSession = Depends(database), current_user : UserM = Depends(get_current_user)):
    try:
        return await user_image(file, db, current_user)
    except Exception as i:
        raise HTTPException(400, str(i))



@user_router.delete('/delete_self')
async def ozini_ochirish(db:AsyncSession = Depends(database), current_user : UserM = Depends(get_current_user)):
    try:
        return await delete_self(db, current_user)
    except Exception as j:
        raise HTTPException(400, str(j))

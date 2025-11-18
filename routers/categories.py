from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from functions.categories import add_category, change_category, delete_category
from models.categories import CategoryM
from models.users import UserM
from routers.login import get_current_user
from schemas.categories import CategoryS
from db import get_db

category_router = APIRouter()


@category_router.get('/get_types')
async def turlarni_korish(db:AsyncSession = Depends(get_db)):
    result = await db.execute(select(CategoryM))
    return result.scalars().all()

    
@category_router.post('/post_types')
async def turlar_qoshish(form : CategoryS, db:AsyncSession = Depends(get_db), current_user : UserM = Depends(get_current_user)):
    try:
        return await add_category(form, db, current_user)
    except Exception as f:
        raise HTTPException(400, str(f))



@category_router.put('/put_types')
async def turlarni_tahrirlash(ident:int, form:CategoryS, db:AsyncSession = Depends(get_db), current_user : UserM = Depends(get_current_user)):
    try:
        return await change_category(ident, form, db, current_user)
    except Exception as d:
        raise HTTPException(400, str(d))



@category_router.delete('/delete_types')
async def ozini_ochirish(ident:int, db:AsyncSession = Depends(get_db), current_user : UserM = Depends(get_current_user)):
    try:
        return await delete_category(ident, db, current_user)
    except Exception as j:
        raise HTTPException(400, str(j))
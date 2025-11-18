from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db import Base, engine, get_db
from routers.categories import category_router
from routers.users import user_router, admin_router
from routers.login import login_router
import models


app = FastAPI()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


@app.get("/ping-db")
async def ping_db(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT 1")
    return {"db_status": result.scalar()}



app.include_router(user_router, tags=["Profil"])
app.include_router(admin_router)
app.include_router(login_router)
app.include_router(category_router, tags=["Taom turlari"])
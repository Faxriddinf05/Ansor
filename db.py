from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# DATABASE_URL='mysql+aiomysql://root:IRiugNPzoTQTFAaZVFMjBHqGfbtDnNfT@switchback.proxy.rlwy.net:23954/railway'

engine = create_async_engine('mysql+aiomysql://root@localhost:3306/ansor', echo=True)


AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()


async def database():
    async with AsyncSessionLocal() as db:
        try:
            yield db
        finally:
            await db.close()
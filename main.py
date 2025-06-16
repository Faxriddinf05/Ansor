from fastapi import FastAPI
from routers.categories import category_router
from routers.users import user_router, admin_router
from routers.login import login_router


app = FastAPI()


app.include_router(user_router, tags=["Profil"])
app.include_router(admin_router)
app.include_router(login_router)
app.include_router(category_router, tags=["Taom turlari"])
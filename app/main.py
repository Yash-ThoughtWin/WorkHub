from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION

from app.api.role import router as role_router
from app.api.user import router as user_router


app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

app.include_router(role_router)
app.include_router(user_router)

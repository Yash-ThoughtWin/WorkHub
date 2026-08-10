from fastapi import FastAPI
from app.config import APP_NAME, APP_VERSION

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION
)

@app.get("/")
def welcm():
    return "WELCOME TO WorkHUB"


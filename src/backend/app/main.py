from pathlib import Path
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .auth_routes import auth_router

app = FastAPI(title="REC SCIENCE")

app.include_router(auth_router)


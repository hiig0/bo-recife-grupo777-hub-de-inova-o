from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv

import os

load_dotenv()

from .auth_routes import auth_router
from .projects_routes import projects_router

app = FastAPI(title="REC SCIENCE")

app.include_router(auth_router)
app.include_router(projects_router)

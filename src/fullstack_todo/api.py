from fastapi import FastAPI

from fullstack_todo.config import settings
from fullstack_todo.health.views import router as health_router

app = FastAPI(title=settings.TITLE)

app.include_router(health_router, prefix="/health")

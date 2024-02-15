from fastapi import FastAPI
from backend.core.celery_utils import create_celery

from backend.users import users_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.celery_app = create_celery()

    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}

    return app

from fastapi import FastAPI

from backend.users import users_router


def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(users_router)

    @app.get("/")
    async def root():
        return {"message": "Hello, World!"}

    return app

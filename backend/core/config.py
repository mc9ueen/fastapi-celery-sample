from dotenv import load_dotenv
from pydantic.env_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    celery_broker: str
    celery_backend: str

    class Config:
        env_file = ".env"


settings = Settings()

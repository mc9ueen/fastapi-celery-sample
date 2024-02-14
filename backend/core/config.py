import os
import pathlib
from typing import Optional
from functools import lru_cache

from dotenv import load_dotenv
from pydantic.env_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    fastapi_config: str
    base_dir: Optional[pathlib.Path] = pathlib.Path(__file__).parent.parent.parent
    database_url: Optional[str] = f"sqlite:///{base_dir}/db.sqlite3"
    database_connect_dict: Optional[dict] = {}
    celery_broker: str
    celery_backend: str

    class Config:
        env_file = ".env"


class DevSettings(Settings):
    pass


class ProdSettings(Settings):
    pass


class TestSettings(Settings):
    pass


@lru_cache
def get_settings() -> Settings:
    config_cls_dict = {
        "dev": DevSettings,
        "prod": ProdSettings,
        "test": TestSettings,
    }

    config_name = os.environ.get("FASTAPI_CONFIG", "dev")
    return config_cls_dict[config_name]()


settings = get_settings()

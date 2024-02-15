import os
import pathlib
from functools import lru_cache


class Settings:
    BASE_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent
    DATABASE_URL: str = os.environ.get(
        "DATABASE_URL", f"sqlite:///{BASE_DIR}/db.sqlite3"
    )
    DATABASE_CONNECT_DICT: dict = {}
    CELERY_BROKER_URL: str = os.environ.get(
        "CELERY_BROKER_URL", "redis://127.0.0.1:6379/0"
    )
    CELERY_RESULT_BACKEND: str = os.environ.get(
        "CELERY_RESULT_BACKEND", "redis://127.0.0.1:6379/0"
    )

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

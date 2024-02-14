from kombu.common import declaration_cached
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.core.config import settings


engine = create_engine(
    settings.database_url, connect_args=settings.database_connect_dict
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

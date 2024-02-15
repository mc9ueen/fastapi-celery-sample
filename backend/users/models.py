from sqlalchemy import Column, Integer, String

from backend.core.database import Base


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=True)

    def __init__(self, username, email, *args, **kwargs):
        self.username = username
        self.email = email

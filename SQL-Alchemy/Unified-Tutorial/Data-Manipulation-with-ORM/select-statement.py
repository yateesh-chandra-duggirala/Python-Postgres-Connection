from sqlalchemy import create_engine, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, Session
from typing import Optional, List

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name  = {self.name!r}, full_name = {self.full_name!r})"

# Create a session
session = Session(engine)

obj = session.get(User, 4)

print(obj)
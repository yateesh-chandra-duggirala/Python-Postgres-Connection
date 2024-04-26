from sqlalchemy import create_engine, text, String, ForeignKey
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo= True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user_account"

    # Also, we can declare as
    # id = mapped_column(Integer, primary_key = True)
    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    address : Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name = {self.name!r}, full_name = {self.full_name!r})"

class Address(Base):
    __tablename__ = "address"

    id : Mapped[int] = mapped_column(primary_key= True)
    email : Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user : Mapped[User] = relationship(back_populates="address")

    def __repr__(self) -> str:
        return f"Address(id = {self.id!r}, email = {self.email!r})"
    
Base.metadata.create_all(engine)
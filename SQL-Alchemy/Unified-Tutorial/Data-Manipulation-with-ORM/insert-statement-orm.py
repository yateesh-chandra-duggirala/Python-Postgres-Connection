from sqlalchemy import create_engine, String, ForeignKey
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

    address : Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id = {self.id!r}, name  = {self.name!r}, full_name = {self.full_name!r})"

class Address(Base) :
    __tablename__ = "address"

    id : Mapped[int] = mapped_column(primary_key=True)
    email : Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user : Mapped[User] = relationship(back_populates="address")

    def __repr__(self) -> str:
        return f"Address(id : {self.id!r}, email = {self.email!r}, user_id = {self.user_id!r})"

# Create a session
session = Session(engine)

# Create an object 
likith = User(name = "Likith", full_name = "Likith Kumar")

# Adding Single Object
session.add(likith)

neha = User(name="Neha", full_name="Sri Neha")

# Add bulk items at a time
session.add_all([likith, neha])
# session.flush()
session.commit()
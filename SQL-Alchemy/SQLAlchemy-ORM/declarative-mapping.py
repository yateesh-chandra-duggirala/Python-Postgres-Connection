from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase) :
    pass

class User(Base) : 
    __tablename__ = "user"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str]
    fullname : Mapped[str] = mapped_column(String(30))
    nickname : Mapped[str]
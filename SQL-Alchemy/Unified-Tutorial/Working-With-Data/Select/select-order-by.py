from sqlalchemy import create_engine, String, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from typing import Optional

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User( id : {self.id!r}, name : {self.name!r}, full_name : {self.full_name!r})"

stmt = select(User).order_by(User.name)

# For descending order, we can just use field.desc(): 
# stmt = select(User).order_by(User.name.desc())

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())
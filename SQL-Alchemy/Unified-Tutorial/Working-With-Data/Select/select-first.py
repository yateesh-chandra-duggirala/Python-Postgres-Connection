from sqlalchemy import create_engine, MetaData, String, select, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session, relationship
from typing import Optional, List

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")
meta_data = MetaData()

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "user_account"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(String(30))
    full_name : Mapped[Optional[str]]

    def __repr__(self) -> str:
        return f"User( Id : {self.id!r}, Name : {self.name!r}, full_name : {self.full_name!r})"

# For specific columns :
stmt = select(User.name, User.full_name)

# For all columns 
# stmt = select(User)

with Session(engine) as sess:
    res = sess.execute(stmt).first()
    print(res)
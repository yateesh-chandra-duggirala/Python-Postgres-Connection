from sqlalchemy import create_engine, text, String, ForeignKey, Table, MetaData
# from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo= True)

metadata_object = MetaData()

user_table = Table("user_account", metadata_object, autoload_with=engine)
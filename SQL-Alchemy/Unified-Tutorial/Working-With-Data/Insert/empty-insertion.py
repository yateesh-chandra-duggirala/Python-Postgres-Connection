from sqlalchemy import create_engine, Table, MetaData, insert

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo = True)

metadata_obj = MetaData()
user_table = Table("user_account", metadata_obj, autoload_with=engine)

print(insert(user_table).values().compile(engine))
from sqlalchemy import create_engine, MetaData, select, Table

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)

user_table_1 = user_table.alias()
user_table_2 = user_table.alias()


stmt = select(user_table_1.c.name, user_table_2.c.name).join_from(user_table_1, user_table_2, user_table_1.c.id > user_table_2.c.id)

with engine.connect() as conn:
    result = conn.execute(stmt)
    print(result.all())
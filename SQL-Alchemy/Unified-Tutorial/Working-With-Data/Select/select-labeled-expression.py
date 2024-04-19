from sqlalchemy import create_engine, MetaData, Table, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo = True)

meta_data = MetaData()

user_table = Table("user_account", meta_data, autoload_with=engine)

stmt = select(("Username : " + user_table.c.name).label("username"),).order_by(user_table.c.name)

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result.all())
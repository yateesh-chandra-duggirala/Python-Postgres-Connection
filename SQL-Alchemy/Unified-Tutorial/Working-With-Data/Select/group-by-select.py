from sqlalchemy import func, create_engine, MetaData, Table, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account",meta, autoload_with=engine)
address_table = Table("address",meta, autoload_with=engine)

stmt = select(user_table.c.name, func.count(user_table.c.name).label("count")).group_by(user_table.c.name)

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result.all())
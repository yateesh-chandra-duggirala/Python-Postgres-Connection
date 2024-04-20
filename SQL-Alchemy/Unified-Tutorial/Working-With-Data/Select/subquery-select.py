from sqlalchemy import create_engine, Table, MetaData, select, func

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)
address_table = Table("address", meta, autoload_with=engine)

subq = (select(func.count(address_table.c.id).label("count"), address_table.c.user_id).group_by(address_table.c.user_id).subquery())

print(select(subq.c.user_id, subq.c.count))
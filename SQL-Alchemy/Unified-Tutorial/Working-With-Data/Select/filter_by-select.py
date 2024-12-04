from sqlalchemy import create_engine, Table, MetaData, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)

stmt = select(user_table).filter_by(name = "Yateesh", id = 1)

print(stmt)

with engine.connect() as conn :
    res = conn.execute(stmt)
    print(res.all())
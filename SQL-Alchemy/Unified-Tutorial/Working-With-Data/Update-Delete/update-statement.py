from sqlalchemy import create_engine, Table, MetaData, update, text

meta = MetaData()

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

user_table = Table("user_account", meta, autoload_with=engine)

stmt = update(user_table).where(user_table.c.id == 1).values(full_name = "Yateesh Chandra D")

with engine.connect() as conn :
    res= conn.execute(stmt)
    print(res.rowcount)
    result = conn.execute(text("SELECT * FROM user_account"))
    print(result.all())
    conn.commit()

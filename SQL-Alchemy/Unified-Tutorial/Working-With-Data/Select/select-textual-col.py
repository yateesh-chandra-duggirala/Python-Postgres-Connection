from sqlalchemy import create_engine, MetaData, Table, select, text

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta_data = MetaData()

user_table = Table("user_account", meta_data, autoload_with= engine)

stmt = select(text("'ACC_TAB'"), user_table.c.name, user_table.c.full_name).order_by(user_table.c.name)

with engine.connect() as conn :
    res = conn.execute(stmt)
    print(res.all())
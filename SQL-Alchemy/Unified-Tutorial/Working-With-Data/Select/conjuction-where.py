from sqlalchemy import create_engine, select, MetaData, Table, and_, or_

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db")

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)

stmt = select(user_table).where(
    and_(
        or_(user_table.c.name == "Yateesh", user_table.c.name == "Kranthi"),
        user_table.c.id == 1,
    )
)

with engine.connect() as conn:
    res = conn.execute(stmt)
    print(res.all())
from sqlalchemy import create_engine, literal_column, Table, MetaData, select

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo=True)

meta = MetaData()

user_table = Table("user_account", meta, autoload_with=engine)

stmt = select(literal_column("'some_Phrase'").label("p"), user_table.c.name.label("username")).order_by(user_table.c.full_name)

with engine.connect() as conn :
    result = conn.execute(stmt)
    print(result.all())
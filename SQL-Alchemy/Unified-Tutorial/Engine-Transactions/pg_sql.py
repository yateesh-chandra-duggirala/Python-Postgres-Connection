from sqlalchemy import text, create_engine

pg_engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo=True)

with pg_engine.connect() as conn:
    result = conn.execute(text("select * from sample_table_tv"))
    print(result.all())
from sqlalchemy import text, create_engine

engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as conn:
    result = conn.execute(text("SELECT 'hello world'"))
    print(result.all())


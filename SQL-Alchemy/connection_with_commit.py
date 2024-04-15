from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

create_table = "CREATE TABLE sample (x int, y int)"

with engine.connect() as conn:
    conn.execute(text(create_table))
    conn.execute(
        text("INSERT INTO sample VALUES(:x , :y)"),
        [{"x" : 1, "y" : 1}, {"x" : 2, "y": 4}],
    )
    result = conn.execute(text("SELECT * FROM sample"))
    print(result.all())
    conn.commit()

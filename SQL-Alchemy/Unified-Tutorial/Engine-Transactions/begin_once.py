from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo = True)

with engine.begin() as conn :
    conn.execute(
        text("Insert into sample values(:x , :y)"),
        [{"x" : 3, "y" : 6}, {"x" : 5, "y" : 4}],
    )
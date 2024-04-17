from sqlalchemy.orm import Session
from sqlalchemy import text, create_engine

statement = text("SELECT")

engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

create_table = "CREATE TABLE sample (x int, y int)"

with engine.connect() as conn:
    conn.execute(text(create_table))
    conn.execute(
        text("INSERT INTO sample VALUES(:x , :y)"),
        [{"x" : 1, "y" : 1}, {"x" : 2, "y": 4},{"x" : 3, "y": 27} ],
    )
    conn.commit()

stmt = text("UPDATE sample SET y = :y WHERE x = :x")

with Session(engine) as session :
    result = session.execute(
        stmt,[{"x" : 2, "y" : 8}]
    )
    result = session.execute(text("SELECT * FROM sample"))
    print(result.all())
    session.commit()
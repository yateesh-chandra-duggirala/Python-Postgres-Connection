from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

with engine.connect() as conn:
    conn.execute(text("Create Table math (x int, y int)"))
    conn.execute(
        text("INSERT INTO math values(:x, :y)"),
        [{"x" : 1, "y" : 1}, {"x" : 2, "y" : 4}, {"x" : 3, "y" : 9}, {"x": 4, "y" : 16}],
    )
    conn.commit()
    result = conn.execute(text("SELECT * from math where y > :y"), {"y" : 3})
    print(result.all())
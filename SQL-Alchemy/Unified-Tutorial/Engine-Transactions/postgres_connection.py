from sqlalchemy import create_engine, text

engine = create_engine("postgresql+psycopg2://postgres:postgres@localhost/db", echo=True)

with engine.connect() as conn :
    # conn.execute(text("CREATE TABLE sample (x int, y int)"))
    # conn.execute(
    #     text("INSERT INTO sample values (:x, :y)"),
    #     [{'x' : 1, 'y' : 1}, {'x' : 3, 'y' : 9},{'x' : 2, 'y' : 4}],
    # )
    conn.commit()
    result = conn.execute(text("SELECT * from sample order by x"))
    print(result.all())
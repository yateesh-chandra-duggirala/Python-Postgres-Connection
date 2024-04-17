from sqlalchemy import create_engine, text

engine = create_engine("sqlite+pysqlite:///:memory:", echo= True)

create_table = "CREATE TABLE sample (x int, y int)"

with engine.connect() as conn:
    conn.execute(text(create_table))
    conn.execute(
        text("INSERT INTO sample VALUES(:x , :y)"),
        [{"x" : 1, "y" : 1}, {"x" : 2, "y": 4}],
    )
    conn.commit()
    
    result = conn.execute(text("SELECT x, y from sample"))

    '''
    # 1. Normal Print Statement :
    print("x", "y", sep = "\t|\t")
    print("------" * 3)
    for i in result:
        print(i.x, i.y, sep = "\t|\t")
    '''
    
    '''
    # 2. Tuple Assignment :
    for x, y in result:
        print(x, y)
    '''

    '''
    # 3. Integer Index :
    for row in result :
        x = row[0]
        y = row[1]
        print(x, y)
    '''

    '''
    # 4. Attribute Name
    for row in result :
        x = row.x
        y = row.y
        print("Row :", x, y)
    '''

    # 5. Mapping Access
    for dict_row in result.mappings():
        x = dict_row['x']
        y = dict_row['y']
        print(x, y)

    conn.commit()
    
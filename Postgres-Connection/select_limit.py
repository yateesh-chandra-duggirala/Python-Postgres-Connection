import psycopg2
conn = psycopg2.connect(
    database = "mydb",
    user = "postgres",
    password = "postgres"
)

conn.autocommit = True

cursor = conn.cursor()

sql_statement = "select * from employee limit 2 offset 2"
cursor.execute(sql_statement)
print(cursor.fetchall())
conn.commit()

conn.close()
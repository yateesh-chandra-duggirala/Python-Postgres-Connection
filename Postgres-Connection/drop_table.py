import psycopg2

conn = psycopg2.connect(
    database = 'mydb',
    user = 'postgres',
    password = 'postgres'
)

conn.autocommit = True

cursor = conn.cursor()

drop_sql = "DROP Table Employee"
cursor.execute(drop_sql)
print("Table Dropped....!")
conn.commit()

select_sql = "Select * from Employee"
cursor.execute(select_sql)
print(cursor.fetchall())
conn.commit()

conn.close()
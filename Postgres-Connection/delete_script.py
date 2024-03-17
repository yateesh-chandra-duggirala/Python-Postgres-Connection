import psycopg2

conn = psycopg2.connect(
    database = 'mydb',
    user = 'postgres',
    password = 'postgres'
)

conn.autocommit = True

cursor = conn.cursor()

delete_statement = "DELETE From employee where Age = 25"
cursor.execute(delete_statement)
print("Row Deleted successfully")
conn.commit()

select_statement = "SELECT * from employee"
cursor.execute(select_statement)
print(cursor.fetchall())
conn.commit()

conn.close()
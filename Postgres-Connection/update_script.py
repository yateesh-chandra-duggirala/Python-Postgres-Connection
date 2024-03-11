import psycopg2
conn = psycopg2.connect(
    database = "mydb",
    user = "postgres",
    password = "postgres"    
)
conn.autocommit = True

cursor = conn.cursor()
update_statement = "UPDATE employee set income = 10000 where first_name = 'Tripthi'"
cursor.execute(update_statement)
print("Table Updated...")
conn.commit()

select = "Select * from employee"
cursor.execute(select)
print(cursor.fetchall())
conn.commit()

conn.close()
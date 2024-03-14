import mysql.connector

conn = mysql.connector.connect(
    database = "mydb",
    user = "root",
    password = "03072001"    
)

cursor = conn.cursor()

update_statement = "UPDATE employee set income = income + 3000 where first_name = 'Raj'"
cursor.execute(update_statement)

print("Table Updated...")

conn.commit()

select = "Select * from employee"
cursor.execute(select)
print(cursor.fetchall())

conn.commit()
conn.close()
import mysql.connector

conn = mysql.connector.connect(
    database = "mydb",
    user = "root",
    password = "03072001"
)

cursor = conn.cursor()

# Write a query to Limit the Rows
limit_statement = "select * from employee limit 2"
cursor.execute(limit_statement)
limit_result = cursor.fetchall()
print(limit_result)

# Write a Query to limit the Rows with offset
offset_statement = "select * from employee limit 2 offset 3"
cursor.execute(offset_statement)
offset_result = cursor.fetchall()
print(offset_result)

conn.commit()

conn.close()
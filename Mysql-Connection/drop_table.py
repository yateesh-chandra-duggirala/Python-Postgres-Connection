import mysql.connector

conn = mysql.connector.connect(
    database = 'mydb',
    user = 'root',
    password = '03072001'
)

cursor = conn.cursor()

drop_sql = "DROP Table Cricketers"
cursor.execute(drop_sql)
print("Table Dropped....!")
conn.commit()

select_sql = "Select * from Cricketers"
cursor.execute(select_sql)
print(cursor.fetchall())
conn.commit()

conn.close()
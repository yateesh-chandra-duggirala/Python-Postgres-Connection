import mysql.connector

conn = mysql.connector.connect(
    database = 'mydb',
    user = 'root',
    password = '03072001'
)

cursor = conn.cursor()

delete_statement = "DELETE From employee where Age = 25"

try :
    cursor.execute(delete_statement)
    print("Row Deleted successfully")
    conn.commit()
except : 
    conn.rollback()

select_statement = "SELECT * from employee"
cursor.execute(select_statement)
print(cursor.fetchall())
conn.commit()

conn.close()
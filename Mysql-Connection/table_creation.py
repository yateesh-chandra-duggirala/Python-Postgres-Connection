from mysql.connector import connection

conn = connection.MySQLConnection(
    user = "root",
    password = "03072001",
    database = "mydb",
    host = "localhost",
    port = "3306"
)

cursor = conn.cursor()

create_table = """
                CREATE TABLE EMPLOYEE(
                FIRST_NAME CHAR(20) NOT NULL,
                LAST_NAME CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT
                )
                """
cursor.execute(create_table)
print("Table is successfully created")

cursor.execute("SHOW TABLES")

print(cursor.fetchall())

conn.close()
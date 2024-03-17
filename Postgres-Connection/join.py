import psycopg2

# Establishing the connection
conn = psycopg2.connect(
    database = "mydb",
    user = "postgres",
    password = "postgres"
)

# Set the Auto Commit to True.
conn.autocommit = True

# Design a Cursor Object.
cursor = conn.cursor()

# Create a Table Cricketers and Insert the Data 
create_cricketers = '''
                    CREATE TABLE CRICKETERS (
                        First_Name VARCHAR(255), 
                        Last_Name VARCHAR(255), 
                        Age int, 
                        Place_Of_Birth VARCHAR(255), 
                        Country VARCHAR(255)
                    );
                    '''
cursor.execute(create_cricketers)

insert_cricketers = """INSERT INTO CRICKETERS 
                    ( FIRST_NAME, LAST_NAME, AGE, Place_Of_Birth, Country) VALUES 
                    (%s, %s, %s, %s, %s)"""

cricketers_data = [('Shikhar', 'Dhawan', 33, 'Delhi', 'India'),
        ('Jonathan', 'Trott', 38, 'CapeTown', 'SouthAfrica'),
        ('Kumara', 'Sangakkara', 41, 'Matale', 'Srilanka'),
        ('Virat', 'Kohli', 30, 'Delhi', 'India'),
        ('Rohit', 'Sharma', 32, 'Nagpur', 'India')]

cursor.executemany(insert_cricketers, cricketers_data)
conn.commit()

# Create a Table ODIStats and Insert the Data
create_odiStats =   """
                    CREATE TABLE ODIStats (
                    First_Name VARCHAR(255), 
                    Matches INT, 
                    Runs INT, 
                    AVG FLOAT, 
                    Centuries INT, 
                    HalfCenturies INT
                    );
                    """
cursor.execute(create_odiStats)

insert_odi =    """INSERT INTO ODIStats 
                    ( First_Name, Matches, Runs, Avg, Centuries, HalfCenturies) VALUES 
                    (%s, %s, %s, %s, %s, %s)"""

data_odi = [('Shikhar', 133, 5518, 44.5, 17, 27),
            ('Jonathan', 68, 2819, 51.25, 4, 22),
            ('Kumara', 404, 14234, 41.99, 25, 93),
            ('Virat', 239, 11520, 60.31, 43, 54),
            ('Rohit', 218, 8686, 48.53, 24, 42)]
cursor.executemany(insert_odi, data_odi)
conn.commit()

join_script = "SELECT * from Cricketers c inner join ODIStats o on c.first_name = o.first_name"

cursor.execute(join_script)
print(cursor.fetchall())
conn.commit()

conn.close()
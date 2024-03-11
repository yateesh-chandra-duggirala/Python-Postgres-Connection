# Python PostgreSQL Connection
## Connecting from PSQL Shell
- PostgreSQL provides its own shell to execute queries.
- To establish the connection with the postgresql database, make sure that you have installed it properly in the system.
- If you are able to connect to your database, We are good to go.

## Connecting from Python
- The connection class of the psycopg2 represents/ handles an instance of a connection.
- psycopg2 (Psychotic Postgres 2.0) is a Database adapter that connects Python and Postgres

### 1. Establishing connection :
- New connections can be created using the connect() function.
- This accepts the basic connection parameters such as dbname, user, password, host, port, and returns a connection object.
- Using this function, we can establish a connection with the postgreSQL.
- If the database does not exist, then it will be created and finally a database object will be returned.
- Refer to [connection.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/connection.py) for better understanding

### 2. Creating database :
- The cursor class of psycopg2 provides various methods execute various postgreSQL Commands, fetch records and copy data.
- A cursor object can be created using the cursor() method of the connection class.
- The execute() method of this class accepts a postgresql query as a parameter and executes it.
- In order to create a database in postgreSQL execute the CREATE DATABASE query using this method.
- Refer the [database-creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/database_creation.py) script

### 3. Creating Table :
- Let us execute the CREATE TABLE query using execute() method.
- Before that we have to execute another query DROP Table If exists if we want to create a new table instead of the old one.
- View the [table-creation.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/table_creation.py) to understand the working.

### 4. Inserting Rows :
- We have to execute the INSERT Query using the execute() method.
- For clear info, Have a look at the [insertion-script.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/insertion_script.py) script.

### 5. Retrieving Data :
- Read Operation means to fetch some information from the database.
- Data can be fetched using fetch() method provided by the psycopg2
- The Cursor Class provides three methods namely fetchall(), fetchOne() and fetchMany()
a. fetchall() - This method retrieves all the rows in the result set of query and returns them as list of tuples.
b. fetchone() - This method fetches the next row in the result of a query and returns it as a tuple.
c. fetchMany() - This method is similar to fetchOne() but, it retrieves the next set of rows in the result set of a query, instead of a single row.
**A Result Set is an object that is returned when a cursor object is used to query a table.**
- Refer to the [select-statement.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/select_statement.py)

### 6. Where Clause using Python
- To fetch the specific records from a table using the python program execute the select statement with WHERE Clause, by passing it as a parameter to the execute() method.
- Go to [conditional-select.py](https://github.com/yateesh-chandra-duggirala/Python-Database-Connection/blob/master/Postgres-Connection/conditional_select.py) script to learn the steps.


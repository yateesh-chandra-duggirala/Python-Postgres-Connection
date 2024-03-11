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
- Refer to [connection.py](https://github.com/yateesh-chandra-duggirala/Python-Postgres-Connection/blob/master/connection.py) for better understanding

### 2. Creating database :
- The cursor class of psycopg2 provides various methods execute various postgreSQL Commands, fetch records and copy data.
- A cursor object can be created using the cursor() method of the connection class.
- The execute() method of this class accepts a postgresql query as a parameter and executes it.
- In order to create a database in postgreSQL execute the CREATE DATABASE query using this method.
- Refer the [database-creation.py](https://github.com/yateesh-chandra-duggirala/Python-Postgres-Connection/blob/master/database-creation.py) script

### 3. Creating Table :
- Let us execute the CREATE TABLE query using execute() method.
- Before that we have to execute another query DROP Table If exists if we want to create a new table instead of the old one.
- View the [table-creation.py](https://github.com/yateesh-chandra-duggirala/Python-Postgres-Connection/blob/master/table-creation.py)https://github.com/yateesh-chandra-duggirala/Python-Postgres-Connection/blob/master/table-creation.py to understand the working.

# SQLAlchemy :
- Install SQLAlchemy through pip
- Check the version using sqlalchemy.__version__

## The Engine :
- *Engine* : Engine acts a central source of connections for a particular database, providing both factory as well as holding space called Connection Pool for these database connections.
- sqlalchemy provides a class called create_engine() from which an object is created just once for a particular database server and is configured using URL String which will describe how it should connect to the database host or backend.
- For this tutorial, we will use the in-memory-only SQLite database.
- The engine, when first returned  by create_engine() has not actually tried to connect to the database yet, that happens only the first time it is asked to perform a task against the database. This is called lazy-initialization
- we have used echo = True, which will instruct the Engine to log all of the SQL it emits to a Python logger that will write to standard out

## Working with Transactions and DBAPI :
- When using ORM, The Engine is managed by another object called the session.
- The Session emphasizes a transactional and SQL execution pattern that is largely identical to that of connection.
- text() constructor helps us to write SQL Statements as textual SQL

## Getting a Connection :
- The purpose of the engine object from a user-facing perspective is to provide a unit of connectivity to the database called the Connection.
- When working with the core directly, the connection object is how all interaction with the database is done.
- As the connection represents an open resource against the database, we want to always limit the scope of our use of this object.
- The default behavior of the Python DBAPI includes that a transaction is always in progress; when the scope of the connection is released, a Rollback is emitted to the end of the transaction.
- The Transaction is not committed automatically, when we want to commit, we can make it connection.commit().
- Auto Commit is also available. The result of our SELECT was also returned in an object called Result.
- The object is consumed within the connect block and is not passed along outside of the scope of our connection.

## Committing changes : 
- Inorder to commit the transaction, we use connection.commit().
- There is also another style of committing data, which is that we can declare our connect block to be a transaction block up front.
- For this mode of operation, we use the Engine.begin() method to acquire the connection, rather than the engine.connect().

## Fetching Rows : 
- Result Object is returned when we run the SELECT Query.
- Result object represents an iterable object of result rows.
- Result has lots of methods for fetching and transforming rows, such as the result.all() method returns a list of all Row Objects.
- The Row objects themselves are intended to act like Python named tuples.

### Tuple Assignment : 
- This is the most Python-idiomatic style, which is to assign variables to each row positionally as they are received.
### Integer Index :
- Tuples are Python Sequences, so regular integer access is available too.
### Attribute Name : 
- As these are Python named tuples, the tuples have dynamic attribute names matching the names of each column.
- These names are normally the names that the SQL statements assigns to the columns in each row.
- While they are usually fairly predictable and can also be controlled by labels, in less defined cases they may be subjected to database-specific behaviors.

### Mapping Access : 
- To Receive Rows as Python mapping objects, which is essentially a read-only version of Python's interface to the common dict object, The Result may be transformed into a MappingResult object using the Result.mappings() modifier. 
- This is a result object that yields dictionary-like RowMapping objects rather than Row Objects.

## Sending Parameters :
- SQL Statements are usually accompanied by data that is to be passed with the statement itself, as we saw in the insert example previously.
- The Connection.execute() method therefore also accepts parameters, which are known as bound parameters.
- A rudimentary example might be if we wanted to limit our SELECT Statement only to rows that meet a certain criteria, such as rows where the y value were greater than a certain value that is passed into a function.
- the text() construct accepts these using a colon format ":y".
- The actual value for ":y" is then passed as the second argument to Connection.execute() in the form of a dictionary.
- In the logged SQL Output, we can see that the bound parameter :y was converted into a question mark when it was sent to the SQLite database.
- This is because the SQLite database driver uses a format called "qmark parameter style", which is one of six different formats allowed by the DBAPI specification.
- SQLAlchemy abstracts these formats into just one, which is the named format using a colon.
- Textual SQL is not the way we work with SQLAlchemy.
- However when using textual SQL, a Python Literal value, even non-integers or dates, should never be stringified into SQL string directly, A parameter should always be used.
- This is most famously known as how to avoid SQL injection attacks when the data is untrusted.
- However it also allows the SQLAlchemy dialects and / or DBAPI to correctly handle the incoming input for the backend.
- Outside of plain textual SQL Use cases, SQLAlchemy's Core Expression API otherwise ensures that Python Literal values are passed as bound parameters where appropriate.

## Executing with an ORM Session :
- The fundamental transactional/ database interactive object when using the ORM is called the Session.
- This session object is used in a manner very similar to that of the connection, and in fact as the Session is used, it refers to a connection internally which it used to emit SQL.
- When the session is used with Non-ORM constructs, It passes through the SQL statements we give it and does not generally do much differently from how the connection does directly.
- The Session has a few different creational patterns, One among them is to construct it within a context manager.

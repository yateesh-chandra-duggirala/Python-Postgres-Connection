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


## Working with Database Metadata : 
- The Central element of the both SQL-Alchemy Core and ORM is the SQL Expression Language which allows for fluent , composable construction of queries.
- The Foundation of these queries are Python objects that represent the Database concepts like tables and columns, collectively known as Database Metadata.
- The most common foundational objects for database metadata in SQL Alchemy are : Metadata, Table, Columns

### Setting up Metadata with Table Objects :
- When we work with a Relational Database, the basic data-holding structure in the database which we query from is known as a table.
- In SqlAlchemy, The database table is ultimately represented by a python object similarly named Table.
- To start using the SQLAlchemy Expression Language, we will want to have Table objects constructed that represent all of the database tables we are interested in working with.
- The table is constructed programmatically either directly by using the Table Constructor, or indirectly by using the ORM Mapped Classes.
- There is also the option to load some or all table information from an existing Database called Reflection.
- Whichever kind of approach is used, we always start out with a collection that will be where we place our tables known as the Metadata object.
- This object is essentially a facade around a Python dictionary that stores a series of table Objects keyed to their String name.
- While the ORM provides some options on where to get this collection, we always have the option to simply make one directly.
- Once we have Metadata Objetc we can declare some Table Objects.
- When not using ORM Declarative models at all, we construct each Table object directly, typically assigning each to a variable that will be how we will reefer to the table in application mode.

- Having a single Metadata Object for an entire application is the most common case, represented as a module-level variable in a single place in an application, often in a "models" or "dbschema" type of package.
- it is also very common that the metadata is accessed via an ORM-centric registry or Declarative Base base class, so that this same metadata is shared among ORM-and Core-declared Table Objects.
- there can be multiple Metadata Collections as well; Table objects can refer to Table objects in other collections without restrictions.
- However, for groups of Table objects that are related to each other, it is in practice much more straight forward to have set them up within a single Metadata Collection, both from the perspective of declaring them, as well as from the perspective of DDL (i.e, CREATE and DROP) statements being emmitted in the correct order.

### Components of a table :
- We can observe that the Table construct as written in Python has a resembelance to a SQL CREATE TABLE Statement. Starting with a table name, then listing out each Column, where each column has a name and datatype

a. Table : represents a database table and assigns itself to a Metadata Collection.
b. Column : represents a column in a database table and assigns itself to a Table object. The column usually includes a string name and a type object. The collection of Column Objects in terms of the parent Table are typically accessed via an Associative array located at Table.c
c. Integer / String - these classes represent SQL Datatypes and can be passed to the column with or without necessarily being instantiated. Above, we want to give a length of 30 to the name column, so we instantiated String(30). But for id and full name and we did not specify these, so we can send the class itself.

## Declaring Simple Constraints :
- The first column in the example includes the Column.primary_key parameter which is a shorthand technique of indicating that this column should be a part of the primary key for this table.
- The primary key itself is normally declared implicitly and is represented by the Primary Key Constraint Construct, which we can see on the table.primary_key attribute on the Table object.
- The constraint that is most typically declared explicitly is the ForeignKeyConstraint object corresponds to a database foreign key constraint.
- When we declare tables, that are related to each other, SQLAlchemy uses the presence of these foreign key constraint declarations not only so that they are emitted within CREATE Statements to the database, but also to assist in constructing SQL Expressions.
- A foreignKeyConstraint that involves only a single column on the target table is typically declared using a Column-level shorthand notation via the ForeignKey object.
- Below we declare a second table address that will have a foreign key constraint referring to the user table.
- The full series of steps are included with a Begin/Commit pair to accomodate for transactional DDL.
- The Create process also takes care of emitting CREATE statements in the correct order; above, the FOREIGN KEY constraint is dependent on the User table existing, so the address table is created second.
- The Metadata Object also features a MetaData.drop_all() method that will emit DROP statements in the reverse order as it would emit CREATE in order to Drop schema elements.

## Using ORM Declarative Forms to Define table Metadata :
- The SQLAlchemy ORM provides for a facade around the Table declaration process referred towards as Declarative Table.
- The declarative table process gives us something else called an ORM mapped Class or just class.
- The mapped class is the most common foundational unit of SQL, when using the ORM and in modern SQLAlchemy can also be used quite effectively with Core-centric use as well.
- Some benefits of using Declarative Table : 
    a. A more succint and Pythonic style of setting up column definitions, where python types may be used to represent the SQL Types to be used in the database.
    b. The resulting mapped class can be used to form SQL Expressions that in may cases maintain PEP 484 typing information that is picked up by static analysis tolls such as Mypy and IDE type checkers.
    c. Allows Declaration of table metadata and the ORM mapped class used in persistence/ object loading operations all at once.
- When using the ORM, the process by which we declare Table metadata is usually combined with the process of declaring mapped classes.
- The mapped class in any python class we would like to create, which will then have attributes on it that will be linked to the columns in a database table.
-While there are a few varieties of how this is achieved, the most common style is known as Declarative, and allows us to declare our user-defined classes and table metadata at once.

## Establishing a Declarative Base :
- When using the ORM, The Metadata collection remains present, however it itself is associated with an ORM-only construct commonly referred towards as the Declarative Base.
- The most expedient way to acquire a new Declarative Base is to create a new class that subclasses the SQLAlchemy DeclarativeBase Class.
- Registry refers to the collection called collection, which is the central mapper configuration unit in the SQLAlchemy.
- Registry is automatically created by Declarative Base itself.

## Declaring Mapped Classes : 
- After establishing the Base Class, we can define ORM Mapped Classes for the user_account and address tables in terms of new classes User and Address.
- We illustrate below the most of the modern form of declarative, which is driven from type annotations using a special type Mapped, which indicates attributes to be mapped as particular types.

### Once go through the mapped_class.py and understand the below observations.
- The 2 classes User and Accounts are called as ORM Mapped Classes and are available for use in ORM persistence and Query Operations.
- Each class refers to a Table object that was generated as part of the declarative mapping process, which is named by assigning a string to the DeclarativeBase.__tablename__ attribute. Once the class is created, this generated Table is available from the DeclarativeBase.__table__. This is called Declarative Table Configuration.
- One of the several alternative declaration would have us build the Table object directly, and assign it directly to DeclarativeBase.__table__ , This method is known as Declarative with Imperative Table.
- To indicate columns in the table, we use the mapped_column() construct, in combination with typing annotations based on the Mapped Type.
- This object will generate Column objects that are applied to the construction of the table.
- For columns with simple datatypes and no other options, we can indicate a Mapped type annotation alone, using Simple Python types like int and str to mean Integer and String.
- Customization of how Python Types are interpreted within the Declarative mapping process is very open ended.
- A column is made nullable by making it Optional['<type>']. Also we can explicitly mention mapped_column(nullable = True)
- Two additional attributes User.addresses and Address.user, define a different kind of attribute called relationship(), which features similar annotation-aware configuration style as shown.
- The classes are automatically given an __init__() method if we do not declare on our own.
- To automatically generate a full-featured __init__() method which provides for positional arguments as well as arguments with default keyword values, the dataclasses feature introduces at Declarative DataClass Mapping may be used.
- It is of course always an option to use an explicit __init__() method as well.
- The __repr__() methods are added so that we get a readable string output; there is no requirement for these methods to be here.
- As is the case with __init__(), a __repr__() method can be generated automatically by using the dataclasses feature.

## Emitting DDL to the Database from an ORM Mapping :
- As our ORM mapped classes refer to Table objects contained within a Metadata Collection, emmitting DDL given the Declarative Base uses the same process as that described previously at Emitting DDL to the Database.
- We have generated the user and address tables in our Database.
- if we had not done so already, we would be free to make use of the Metadata associated with our ORM Declarative Base Class in order to do so, by accessing the collection from the DeclarativeBase.metadata attribute and then using Metadata.create_all() as before.

## Working with Data :
    Let us understand how the Various Manipulation Commands work.
### Insert Statements :
- When using Core as well as when using the ORM for bulk operations, a SQL Insert Statement is generated directly using the insert() function. This function generates a new instance of Insert which represents an INSERT Statement in SQL, that adds new data into a table.

a. The insert() SQL Expression Construct :
- We create a variable that is an instance of Insert.
- most SQL Expressions can be stringified in place as a means to see the general form of what is being produced.
- Execute the query.

b. insert Many :
- We can pass multiple parameters through the form of list of dictionaries.
- The connection ensures that column names which are passed will be expressed in the values clause of the insert statement automatically.

#### Scalar Subquery : 
- A Scalar Subquery is constructed, making use of the select() method and the parameters used in the Sub-Query are set up using an explicit bound parameter name, established using bindparam() construct.

c. Insert Returning : 
- The RETURNING Clause for supported backends is used automatically in order to retrieve the last inserted primary key value as well as the values for server defaults.
- However the Returning clause may also be specified explicitly using the insert.returning.

### Select Statement :
- For both Core and ORM, the select() function generates a Select construct which is used for all SELECT queries. Passed to Methods like Connection.execute() in Core and Session.execute() in ORM, A Select statement is emitted in the current transaction and the result rows available via the returned Result object.
- label is used with select but serves as alias in SQL.
- We are being provided the order_by method which works similar to the order by concept in SQL.
- literal_column is same as text() construct except that instead of representing arbitrary SQL of any form , it explicitly represents a single column and can be labelled towards in subqueries and expressions.
- AND Statement can be invoked using multiple where statements.
- We can Join the tables using join_from in select, which requires the 2 table names in which the join has to be performed
- join() is used from select, which needs any table as an argument and indicates only right side of the join, left side is inferred.
- also we can join table with `select().select_from(table1).join(table2, table1.col == table2.col)`
- we can also use attributes like : isouter = True/ False and full = True / False.
- order_by() can be used with select() in order to order the items. For Descending : order_by(field.desc())
- group_by() can be used with select(), but when we want to use count() from func.
- similarly, group_by can be followed by having clause()
- aliases can be done with the help of alias() method.
- ORM Entity has aliased() function, which may be applied to an entity such as user_account and address.
- We can use CTEs with the help of cte() and subqueries with the help of subquery().

### Working with SQL Functions :
- The func object also provides the various functions 
- func.lower() returns the lower case of the string passed as query.

### Update Statement :
- update() construct is used to update the values from the table.
- The statement that has to be written in set phrase will be written in values() phrase
- And the condition that we write in the where clause will be written as usual.

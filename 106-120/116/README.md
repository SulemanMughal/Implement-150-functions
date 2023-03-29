# Exercise No. 116


**Note:** This exercise requires basic knowledge of SQL.

**sqlite3 documentation:** https://docs.python.org/3/library/sqlite3.html


The following SQL command creates a table named Product with columns: Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice and some column constraints such as INTEGER PRIMARY KEY or NOT NULL:


    CREATE TABLE Customer (Id INTEGER PRIMARY KEY, FirstName TEXT NOT NULL, LastName TEXT NOT NULL)


Implement a function called `generate_sql()` that takes three arguments:

-   *table_name* - table name (str)

-   *col_names* - column names (list, tuple)

-   *constraints* - constraints for columns (list), empty string means no column constraint

The `generate_sql()` function generates SQL code that creates a table named table_name with columns col_names and their constraints.


**Example:**


    [IN]: generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL'])
    [OUT]: 'CREATE TABLE Customer (Id INTEGER PRIMARY KEY, FirstName TEXT NOT NULL)'


**Example:**


    [IN]: generate_sql('Product', ['Id', 'QuantityName'], ['INTEGER PRIMARY KEY', '']
    [OUT]: 'CREATE TABLE Product (Id INTEGER PRIMARY KEY, QuantityName)'


You just need to implement the `generate_sql()` function. The tests run several test cases to validate the solution.
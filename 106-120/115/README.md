# Exercise No. 115


**Note:** This exercise requires basic knowledge of SQL.

**sqlite3 documentation:** https://docs.python.org/3/library/sqlite3.html


The following SQL command creates a table named Product with columns: Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice:


    CREATE TABLE Product (Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice)


Implement a function called `generate_sql()` that takes two arguments:

-   *table_name* - table name (str)

-   *col_names* - column names (list, tuple)

The `generate_sql()` function generates the SQL code that creates the table named table_name with the columns col_names. In this exercise, we ignore any table / column constraints.


**Example:**


    [IN]: generate_sql('Product', ['Id', 'ProductName'])
    [OUT]: 'CREATE TABLE Product (Id, ProductName)'


**Example:**


    [IN]: generate_sql('Customer', ['Id', 'FirstName', 'LastName', 'Age'])
    [OUT]: 'CREATE TABLE Customer (Id, FirstName, LastName, Age)'


You just need to implement the `generate_sql()` function. The tests run several test cases to validate the solution.
# Exercise No. 117


**Note:** This exercise requires basic knowledge of SQL.

**sqlite3 documentation:** https://docs.python.org/3/library/sqlite3.html


The following SQL command creates a table named Product with columns: Id, ProductName, SupplierId, CategoryId, Quantity, UnitPrice:


    CREATE TABLE Customer (
        Id INTEGER PRIMARY KEY, 
        FirstName TEXT NOT NULL, 
        LastName TEXT NOT NULL
    )


This command is properly formatted (for better code readability). The indentation applied is obtained by inserting a tab character for each subsequent column.

Modify the `generate_sql()` function from the previous exercise to obtain the code formatting described above.


    def generate_sql(table_name, col_names, constraints):
        cols = [" ".join((col, constraint)).strip() 
                for col, constraint in zip(col_names, constraints)]
        return f'CREATE TABLE {table_name} (' + ', '.join(cols) + ')'


**Example:**


    [IN]: generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL'])
    [OUT]: 'CREATE TABLE Customer (\n\tId INTEGER PRIMARY KEY,\n\tFirstName TEXT NOT NULL\n)'


**Example with print() function:**


    [IN]: print(generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))


**Output:**


    CREATE TABLE Customer (
        Id INTEGER PRIMARY KEY,
        FirstName TEXT NOT NULL
    )


**Example:**


    [IN]: columns = ['Id', 'QuantityName', 'SuppliedId', 'CategoryId']
    [IN]: constraints = ['INTEGER PRIMARY KEY', 'TEXT NOT NULL', 'INTEGER NOT NULL', 'INTEGER NOT NULL']
    [IN]: generate_sql('Product', columns, constraints)
    [OUT]: 'CREATE TABLE Product (\n\tId INTEGER PRIMARY KEY,\n\tQuantityName TEXT NOT NULL,\n\tSuppliedId INTEGER NOT NULL,\n\tCategoryId INTEGER NOT NULL\n)'


**Example with print() function:**


    [IN]: print(generate_sql('Product', columns, constraints))

**Output:**


    CREATE TABLE Product (
        Id INTEGER PRIMARY KEY,
        QuantityName TEXT NOT NULL,
        SuppliedId INTEGER NOT NULL,
        CategoryId INTEGER NOT NULL
    )


You just need to implement the `generate_sql()` function. The tests run several test cases to validate the solution.
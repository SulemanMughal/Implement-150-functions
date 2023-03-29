# Exercise No. 44

Suppose you implement some ETL process. As input you get CSV files with the following structure:


    open,high,low,close
    45.3,46.1,45.3,45.4
    45.4,46.5,45.0,45.4
    ...


Define a function called `transform()` that takes one argument:

-   *row* - one row of data from the CSV file with the above form (omitting the row with column names)

and returns a dictionary with the following structure:


    {'close': 45.4, 'high': 46.1, 'low': 45.3, 'open': 45.3}


**Example:**


    [IN]: transform('45.3,46.1,45.3,45.4')
    [OUT]: {'close': 45.4, 'high': 46.1, 'low': 45.3, 'open': 45.3}


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
# Exercise No. 147


Define a function called `to_csv()` that will generate a comma separated string (CSV) from any number of keyword arguments so that the keys are CSV column names (see below).


**Examples:**


    [IN]: to_csv(name='John', age=32, country='USA')
    [OUT]: 'name,age,country\nJohn,32,USA'


    [IN]: to_csv(name='John', age=32)
    [OUT]: 'name,age\nJohn,32'


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
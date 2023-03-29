# Exercise No. 22

Define a function called `sort_tuple()` that takes as an argument a list of tuples with the given structure:


    [('mike', 34), ('bob', 41), ('john', 36), ('leo', 28)]


and sorts the list by the second element of the tuple. Expected result:


    [('leo', 28), ('mike', 34), ('john', 36), ('bob', 41)]


**Example:**


    [IN]: sort_tuple([('mike', 34), ('bob', 41), ('john', 36), ('leo', 28)])
    [OUT]: [('leo', 28), ('mike', 34), ('john', 36), ('bob', 41)]


    [IN]: sort_tuple([('mike', 'music'), ('bob', 'art'), ('john', 'math'), ('leo', 'english')])
    [OUT]: [('bob', 'art'), ('leo', 'english'), ('john', 'math'), ('mike', 'music')]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
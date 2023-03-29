# Exercise No. 33

Define a function called `flatten()` that takes a nested list or a tuple as an argument and returns its flattened form (see below):


    ([5], [6], [2], [3]) -> [5, 6, 2, 3]
    ([5], [6], [2, 4, 2], [3, 4]) -> [5, 6, 2, 4, 2, 3, 4]


**Examples:**


    [IN]: flatten(([5], [6], [2], [3]))
    [OUT]: [5, 6, 2, 3]


    [IN]: flatten(([5], [6], [2, 4, 2], [3, 4]))
    [OUT]: [5, 6, 2, 4, 2, 3, 4]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
# Exercise No. 9


Define a function called `get_indices()` that takes a list as an argument and returns a list of all indices that contain an element of type str. If the list has no elements of type str, the function returns an empty list.


**Example:**


    [IN]: get_indices(['https://www.e-smartdata.org', 'response', 202, 'code'])
    [OUT]: [0, 1, 3]


    [IN]: get_indices(['Q', 34, 'DQ', True])
    [OUT]: [0, 2]


    [IN]: get_indices([4, 3, 5, 2])
    [OUT]: []


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
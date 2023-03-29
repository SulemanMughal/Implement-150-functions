# Exercise No. 19

Define a function called `create_mask()` that takes two lists and returns a list that is a logical mask - assuming 1 when those lists have the same value in their respective positions, on the contrary 0.


**Example:**


    [IN]: create_mask([4, 5, 7, 2, 8, 10], [3, 5, 4, 2, 8, 12])
    [OUT]: [0, 1, 0, 1, 1, 0]


    [IN]: create_mask([2, 4, 1], [2, 3, 1])
    [OUT]: [1, 0, 1]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
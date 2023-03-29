# Exercise No. 13

Define a function called `sort_by_row()` that takes a nested list as argument (see example below):


    data = [
        [4, 7, 2, 7, 9, 1],
        [6, 3, 2, 8, 8],
        [9, 7, 3, 2, 7]
    ]


and sorts it in ascending order of each inner list.


**Expected result:**


    [[1, 2, 4, 7, 7, 9], [2, 3, 6, 8, 8], [2, 3, 7, 7, 9]]


**Example:**


    [IN]: sort_by_row([[4, 7, 2, 7, 9, 1], [6, 3, 2, 8, 8], [9, 7, 3, 2, 7]])
    [OUT]: [[1, 2, 4, 7, 7, 9], [2, 3, 6, 8, 8], [2, 3, 7, 7, 9]]


    [IN]: sort_by_row([[5, -2, 3, 7, 4], [6, 3]])
    [OUT]: [[-2, 3, 4, 5, 7], [3, 6]]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.



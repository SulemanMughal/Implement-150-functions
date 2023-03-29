# Exercise No. 14

Define a function called `top3()` that takes a nested list as argument (see example below):


    data = [
        [4, 7, 2, 5, 9, 1, 3],
        [6, 3, 2, 8, 8, 7],
        [9, 7, 3, 2, 7, 2]
    ]


and returns the three largest values from each internal list sorted in descending order (see below). We assume that each internal list has at least three elements.


**Expected result:**


    [[9, 7, 5], [8, 8, 7], [9, 7, 7]]


**Example:**


    [IN]: top3([[4, 7, 2, 7, 9, 1, 3], [6, 3, 2, 8, 8, 7], [9, 7, 3, 2, 10, 2]])
    [OUT]: [[9, 7, 7], [8, 8, 7], [10, 9, 7]]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
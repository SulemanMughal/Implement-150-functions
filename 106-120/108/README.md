# Exercise No. 108

Below is an example of a 3x3 square matrix of numbers in spiral order:


    [1, 2, 3]
    [8, 9, 4]
    [7, 6, 5]


An example of a 4x4 square matrix of numbers in spiral order:


    [ 1,  2,  3, 4]
    [12, 13, 14, 5]
    [11, 16, 15, 6]
    [10,  9,  8, 7]


We move clockwise, starting with the number 1 and increasing by 1.

Implement a function called `spiral_matrix()` that takes the size of the matrix as an argument and generates the matrix in spiral order with the given size. Present the solution in the form of nested lists.


**Tip:** You can use the *itertools* built-in module and the *cycle* class in your solution.


**Example:**


    [IN]: spiral_matrix(1)
    [OUT]: [[1]]


**Example:**


    [IN]: spiral_matrix(2)
    [OUT]: [[1, 2], [4, 3]]


**Example:**


    [IN]: spiral_matrix(3)
    [OUT]: [[1, 2, 3], [8, 9, 4], [7, 6, 5]]


You just need to implement the `spiral_matrix()` function. The tests run several test cases to validate the solution.



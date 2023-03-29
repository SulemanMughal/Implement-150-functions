# Exercise No. 17

Define a function called `calculate()` that takes two arguments:

-   a list of numbers
-   natural number k - default value 5

The function is to return all elements of the list that are distant from their neighbors by the value of k or more. The extreme elements (first and last element) should be omitted from the result.


**Example:**


    [IN]: calculate([2, 6, 2, 8, 1, 3, 10, 3])
    [OUT]: [8, 10]


    [IN]: calculate([1, 6, 5, 2, 8, 11, 3, 10, 3], 3)
    [OUT]: [2, 8, 11, 3, 10]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
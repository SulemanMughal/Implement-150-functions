# Exercise No. 76

Implement a function called `max_prob()` that returns the highest probability value for a given row in a two-dimensional matrix. We assume that the user passes the matrix as a nested list with non-negative elements and sum of each row equal to 1.


**Arguments:**

-   *array* - nested list (two-dimensional matrix, row adds up to one)


**Example:**


    [IN]: max_prob([[0.3, 0.4, 0.3], [0.0, 0.1, 0.9]]) 
    [OUT]: [[0.4], [0.9]]


    [IN]: max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2]])   
    [OUT]: [[0.4], [0.7]]


    [IN]: max_prob([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.4, 0.3, 0.3]]) 
    [OUT]: [[0.4], [0.7], [0.4]]




**Note:** You only need to implement this function.
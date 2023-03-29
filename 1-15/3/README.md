# Exercise No. 3

Two functions are given below:


    def is_nested(array):
        if len(array) == 0:
            return False
        return all(isinstance(row, list) for row in array)
     
     
    def is_all_equal(iterator):
        return len(set(iterator)) <= 1


Define a function called `is_valid_array()` that checks if a matrix can be built from the passed list. You can use the given functions in your solution. The passed list must be a nested list, and each nested list should consist of the same number of elements.


**Example:**


    [IN]: is_valid_array([[3], [4]])
    [OUT]: True


    [IN]: is_valid_array([[3, 4], [4, 5]])
    [OUT]: True


    [IN]: is_valid_array([[3, 4, 5], [4, 5]])
    [OUT]: False


    [IN]: is_valid_array([[3, 4], [4, 5], [3, 1]])
    [OUT]: True


    [IN]: is_valid_array([[]])
    [OUT]: True


You don't need to implement validation in your solution.


**Note!** You only need to define the function.



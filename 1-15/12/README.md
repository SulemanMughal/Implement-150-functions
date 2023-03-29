# Exercise No. 12


Define a function called `concat()` that takes two nested lists as two arguments and returns a new list that will concatenate the nested list items at their respective positions (see below).

An example of nested lists:


    [[6, 2], [6, 3, 7], [3, 5]]
    [[3], [4, 2], [0, 5, 1, 5]]


**Expected result:**


    [[6, 2, 3], [6, 3, 7, 4, 2], [3, 5, 0, 5, 1, 5]]


Please do some validation before concatenating the lists. Check if the lists are the same length. If not, raise `ValueError` with the message `'The given lists are not of the same length.'`


**Example:**


    [IN]: concat([[6, 2], [6, 3, 7], [3, 5]], [[3], [4, 2], [0, 5, 1, 5]])
    [OUT]: [[6, 2, 3], [6, 3, 7, 4, 2], [3, 5, 0, 5, 1, 5]]


    [IN]: concat([[6, 2, 5, 2], [6, 3, 7]], [[4, 2], [0, 5, 1, 5]])
    [OUT]: [[6, 2, 5, 2, 4, 2], [6, 3, 7, 0, 5, 1, 5]]


    [IN]: concat([[6, 2, 5, 2], [6, 3, 7]], [[4, 2], [0, 5, 1, 5], [4]])
    [OUT]: ValueError: The given lists are not of the same length.


**Note!** You only need to define the function.
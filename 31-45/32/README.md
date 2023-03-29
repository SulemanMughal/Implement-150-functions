# Exercise No. 32

Define a function called `preprocess()` that takes a list of tuples as an argument and removes from that list any tuples that contain only `None` values (see below):


    [(4, 5), (4,), (5, None), (5, 3, 2), (None,)] -> [(4, 5), (4,), (5, None), (5, 3, 2)]


Notice that the tuple `(5, None)` remains in the result because it contains an element 5.


**Examples:**


    [IN]: preprocess([(4, 5), (4,), (5, None), (5, 3, 2), (None,)])
    [OUT]: [(4, 5), (4,), (5, None), (5, 3, 2)]


    [IN]: preprocess([(5, None), (None,), (3, None, None), (None, None)])
    [OUT]: [(5, None), (3, None, None)]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
# Exercise No. 133

Functional programming. Consider the following problem. We have an iterable object, for example a list`[3, 6, 8, 10]` and we would like to perform the following operations on the elements of the list:


    (((3 + 6)) + 8) + 10 = (9 + 8) + 10 = 17 + 10 = 27


So we take the first item of the list, add a second item to it, then add another item, and so on until all items in the list are exhausted. The result will be the single value 27 - the sum of all elements.

Note that we have three steps. Each step is adding two numbers. We can represent such a single step with a simple function, for example:


    def add(x, y):
        return x + y


or in a lambda notation (anonymous function):


    lambda x, y: x + y


In conclusion, we reduce the iterable object to some final value using a reducing function. There are three steps in such a process:

-   Calling a function on the first two elements of the iterable object and generating a partial result

-   Calling a function on a partial result and the next element of the iterable object

-   Repeating the process until all elements in the iterable object are exhausted, and return the result

Modify the `reduce()` function from the previous exercise into a function called `reduce_with_start()` so that it takes a third argument called start, which will be the starting value in the reduction process.


**Example:**


    [IN]: reduce_with_start(lambda x, y: x + y, [1, 2, 3, 4], 100)
    [OUT]: 110


**Example:**


    [IN]: reduce_with_start(lambda x, y: x + y, [], 200)
    [OUT]: 200


**Example:**


    [IN]: reduce_with_start(lambda x, y: x + y, [' ', '3', '.', '9'], 'python')
    [OUT]: 'python 3.9'


**Example:**


    [IN]: reduce_with_start(lambda x, y: x + y, [[3, 4], [8, 4], [9, 1]], [6, 7, 4, 10])
    [OUT]: [6, 7, 4, 10, 3, 4, 8, 4, 9, 1]


You just need to implement the `reduce_with_start()` function. The tests run several test cases to validate the solution.
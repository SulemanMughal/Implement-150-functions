# Exercise No. 132

Functional programming. Consider the following problem. We have an iterable object, for example a list `[3, 6, 8, 10]` and we would like to perform the following operations on the elements of the list:


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


Implement a function called `reduce()` that takes two arguments:

-   function - function used to reduce an iterable object

-   iterable - iterable object

and reduces the iterable object with the function (return the result).  If an empty iterable object is passed, the function should return the value None.


**Example:**


    [IN]: reduce(lambda x, y: x + y, [1, 2, 3, 4])
    [OUT]: 10


**Example:**


    [IN]: reduce(lambda x, y: x + y, [])
    [OUT]: None


**Example:**


    [IN]: reduce(lambda x, y: x + y, ['p', 'y', 't', 'h', 'o', 'n'])
    [OUT]: 'python'


**Example:**


    [IN]: reduce(lambda x, y: x + y, [[3, 4], [8, 4], [9, 1]])
    [OUT]: [3, 4, 8, 4, 9, 1]


You just need to implement the `reduce()` function. The tests run several test cases to validate the solution.
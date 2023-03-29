# Exercise No. 100

Consider a simple number compression algorithm that works as follows:


    111155522500 -> [('1', 4), ('5', 3), ('2', 2), ('5', 1), ('0', 2)]


The algorithm goes from left to right through each digit and returns a list of two-element tuples. Each tuple consists of a digit and the number of repetitions of a given digit until the next, different digit in the number is encountered.

Implement a function called `compress()` that compresses number as described above.


**Examples:**


    [IN]: compress(111)
    [OUT]: [('1', 3)]


    [IN]: compress(1000000)
    [OUT]: [('1', 1), ('0', 6)]


    [IN]: compress(10005000)
    [OUT]: [('1', 1), ('0', 3), ('5', 1), ('0', 3)]


**Tip:** You can use the *itertools* built-in module and the *groupby* class in your solution.


You just need to implement the function. The  tests run several test cases to validate the solution.
# Exercise No. 102

Consider a simple number compression algorithm that works as follows:


    111155522500 -> '1....5...2..5.0..'


The algorithm goes from left to right through the number and returns an object of *str* type. Each encountered digit is stored along with the number of dots - the number of times the given digit repeats until it encounters the next, different digit in the number.

Implement a function called `compress()` that compresses number as described above.


**Examples:**


    [IN]: compress(1000040000)
    [OUT]: '1.0....4.0....'


    [IN]: compress(20000000)
    [OUT]: '2.0.......'


    [IN]: compress(123456)
    [OUT]: '1.2.3.4.5.6.'


**Tip:** You can use the *itertools* built-in module and the *groupby* class in your solution.


You just need to implement the function. The  tests run several test cases to validate the solution.
# Exercise No. 101


Consider a simple number compression algorithm that works as follows:


    111155522500 -> '14_53_22_51_02'


The algorithm goes from left to right through the number and returns an object of type *str*. Each encountered digit is stored along with the number of times that digit repeats until another digit is encountered in the number. Each such pair is separated by the `'_'` character.

Implement a function called `compress()` that compresses number as described above.


**Examples:**


    [IN]: compress(100000)
    [OUT]: '11_05'


    [IN]: compress(9993330)
    [OUT]: '93_33_01'


    [IN]: compress(6540000)
    [OUT]: '61_51_41_04'


**Tip:** You can use the *itertools* built-in module and the *groupby* class in your solution.


You just need to implement the function. The  tests run several test cases to validate the solution.
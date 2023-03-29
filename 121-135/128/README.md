# Exercise No. 128

**Binary number system** is a positional numeral system employing 2 as the base and so requiring only two different symbols for its digits, 0 and 1, instead of the usual 10 different symbols needed in the decimal system. The numbers from 0 to 10 are thus in binary 0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, and 1010.

For example, the number 10 in binary can be represented as 1010 because:

1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 8 + 0 + 2 + 0 = 10


How to easily convert a number from decimal to binary?

We can use a simple algorithm:

-   Find the remainder when dividing a number by 2 (this will be the rightmost number in binary)

-   Divide a number by 2 using integer division - //

-   Repeat the above steps until the number is greater than 0.


Implement a function called `decimal_to_binary()` that converts a number from decimal to binary using the above algorithm. Remember about 0.


Python has a built-in function to convert a number to binary called `bin()`, but we will not use it in this exercise.


**Example:**


    [IN]: decimal_to_binary(123)
    [OUT]: '1111011'


**Example:**


    [IN]: decimal_to_binary(3456)
    [OUT]: '110110000000'


**Example:**


    [IN]: decimal_to_binary(0)
    [OUT]: '0'


You only need to implement the `decimal_to_binary()` function. The tests run several test cases to validate the solution.
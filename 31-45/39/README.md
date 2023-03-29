# Exercise No. 39

Define a function called `collatz()` that represents the [Collatz problem](https://en.wikipedia.org/wiki/Collatz_conjecture). The problem can be summarized as follows:


*Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat this process indefinitely. The hypothesis is that no matter what number you start with, you'll always hit 1 in the end.*


The `collatz()` function is supposed to return the number of steps required to reach 1. For example, calling collatz(8) will go through the steps:


    Krok 0: 8
    Krok 1: 4
    Krok 2: 2
    Krok 3: 1


Hence, the number of steps to reach 1 for the number 8 is 3 steps.


**Examples:**


    [IN]: collatz(8)
    [OUT]: 3


    [IN]: collatz(14)
    [OUT]: 17


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
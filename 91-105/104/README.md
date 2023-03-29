# Exercise No. 104

Let's consider vectors consisting of only ones and zeros. Let us also assume an additional convention for representing such a vector. For example, a vector:


    u = [0, 1, 1, 0, 1, 0, 1, 0]


we will present as a sequence:


    '01101010'


For the vectors so defined, we can determine the **Hamming distance**. The Hamming distance of vectors *u* and *v* is the number of elements where the vectors *u* and *v* are different.


**Example:** The Hamming distance of the vectors `'1100100'`, `'1010000'` is equal to 3.


Implement a function called `hamming_distance()` that returns the Hamming distance of two vectors. To calculate the Hamming distance, the vectors must be of the same length. If the vectors are of different lengths raise the ValueError with the following message:

`'Both vectors must be the same length.'`


**Example:**


    [IN]: hamming_distance('01101010', '11011011')
    [OUT]: 4


**Example:**


    [IN]: hamming_distance('110', '10100')
    [OUT]: ValueError: Both vectors must be the same length.


You just need to implement the `hamming_distance()` function. The tests run several test cases to validate the solution.



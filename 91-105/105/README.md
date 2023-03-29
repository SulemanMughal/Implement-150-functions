# Exercise No. 105


Let's consider vectors consisting of only ones and zeros. Let us also assume an additional convention for representing such a vector. For example, a vector:


    u = [0, 1, 1, 0, 1, 0, 1, 0]


we will present as a sequence:


    '01101010'


For the vectors so defined, we can determine the Hamming distance. The Hamming distance of vectors *u* and *v* is the number of elements where the vectors *u* and *v* are different.


**Example:** The Hamming distance of the vectors `'1100100'`, `'1010000'` is equal to 3.


A function called `hamming_distance()` is implemented that returns the Hamming distance of two vectors:


    def hamming_distance(u, v):
        if len(u) != len(v):
            raise ValueError('Both vectors must be the same length.')
        distance = 0
        for i in range(len(u)):
            if u[i] != v[i]:
                distance += 1
        return distance


The weight of the vector u is the Hamming distance of this vector from the zero vector. So in the case of vector `'1001001'` its weight is equal to the Hamming distance of vector `'1001001'` from vector `'0000000'`.


Implement a function called `hamming_weight()` that returns the weight of the vector. In the solution, you can use the `hamming_distance()` function. It is also worth paying attention to a slightly simpler implementation. The weight of a vector is equal to the number of ones in the vector.


**Example:**


    [IN]: hamming_weight('110001010')
    [OUT]: 4


**Example:**


    [IN]: hamming_weight('110111')
    [OUT]: 5


You only need to implement the `hamming_weight()` function. The tests run several test cases to validate the solution.
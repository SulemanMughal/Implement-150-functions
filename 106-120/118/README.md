# Exercise No. 118


In information theory and computer science, the **Levenshtein distance** is a string metric for measuring the difference between two sequences. The Levenshtein distance between two words is the minimum number of single-character operations (insertions, deletions or substitutions) required to change one word into the other.

Single-character operations:

-   inserting a new character into a string

-   removing a character from a string

-   replacing a character in a string with another character

This measure is used in information processing, data processing, machine speech recognition, DNA analysis, plagiarism recognition or spelling correction.


**Example:**


    python
    python3


The Levenshtein distance between the above strings is 1, because one simple operation (insert new character) is enough to transform the first string into the second.


**Example:**


    python
    cython


The Levenshtein distance between the above strings is 1, because one simple operation (replacing a character in a string with another character) is enough to transform the first string to the second.


**Example:**


    c++
    c


Levenshtein's distance between the above strings is 2, because two simple operations (removing two characters from the string) are enough to transform the first string to the second.

Implement a function called `lev()` that calculates the Levenshtein distance of two strings. You can use the formula below:

![Levenshtein](./Levenshtein.png)

Where `|a|` stands for the length of `a` string, and `tail(a)` stands for all string characters except the first. For example, `tail('python')-> 'ython'`. Note that there is a recursion here.


You just need to implement the `lev()` function. The tests run several test cases to validate the solution.
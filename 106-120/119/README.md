# Exercise No. 119

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

A function called `lev()` has been implemented to calculate the Levenshtein distance of two strings:


    def lev(a, b):
     
        if len(b) == 0:
            return len(a)
     
        if len(a) == 0:
            return len(b)
     
        if a[0] == b[0]:
            return lev(a[1:], b[1:])
     
        residual = 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))
        return residual


Consider the following problem. We want to build a simple tool that will allow the user to suggest similar words that the user enters into the system. We will try to use in our solution the Levenshtein distance. We will take a certain bank of words from which we will match the most suitable word, i.e. the one that will have the shortest Levenshtein distance from what the user enters into the system.

We have the following bank of words:


    words = [
        'friend',
        'friends',
        'friendship',
        'fry',
        'data',
        'database',
        'data science'
        'big data',
        'data cleaning',
        'database',
        'date'
    ]


Implement a function called `get_similar()` that will return the top 5 suggestions from our words list for the given user-entered word as shown below.


**Example:**


    [IN]: get_similar('fri')
    [OUT]: [('fry', 1), ('friend', 3), ('friends', 4), ('data', 4), ('date', 4)]


**Example:**


    [IN]: get_similar('dat')
    [OUT]: [('data', 1), ('date', 1), ('fry', 3), ('database', 5), ('big data', 5)]


You just need to implement the `get_similar()` function. The tests run several test cases to validate the solution.



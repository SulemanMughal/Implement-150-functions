# Exercise No. 42

Define a function called `truncate()` that takes two arguments:

-   *heading* - title of the article on the website

-   *length* - number of characters left after truncating the title, by default 30 characters

and returns the abbreviated form of the title up to 30 characters, including three dots at the end ... (see below):


    """Python is a programming language that lets you work quickly
    and integrate systems more effectively."""


    'Python is a programming lan...'


**Examples:**


    [IN]: truncate('Python is a programming language that lets you work quickly.')
    [OUT]: 'Python is a programming lan...'


    [IN]: truncate('Python programming.')
    [OUT]: 'Python programming.'


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
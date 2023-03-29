# Exercise No. 141

The *Stack* class has been implemented.

Implement a function called `is_valid_expression()` that checks if the expression (in the form of a str object) is valid for the number of open and closed parentheses. In this exercise, we take into account the brackets like: (), [], {}.

Examples of valid expressions:

-   '(3 + x) * 2'

-   'for i in range(size):'

Examples of invalid expressions:

-   '(3 + x] * 2'

-   'for i in range(size:'

The function returns True if the expression is valid, on the contrary, False. The function takes one argument.

When implementing `is_valid_expression()` function, think about how you can solve this problem using the stack. For this purpose, use the Stack class.


**Example:**


    [IN]: is_valid_expression('(3 + x) * 2')
    [OUT]: True


    [IN]: is_valid_expression('2 - [(3 + x) * 2)')
    [OUT]: False


You just need to implement the `is_valid_expression()` function. The tests run several test cases to validate the solution.
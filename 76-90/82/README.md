# Exercise No. 82

Using the built-in module *functools* and the *partial* class create from the following function:


    def power(x, y):
        return x ** y


two functions named:

-   *square*

-   *cube*

which will respectively return the square and the cube of the passed argument (functions take only one argument).

Only implement these functions.


**Tip:**


    >>> help(functools.partial)
     
    Help on class partial in module functools:
     
    class partial(builtins.object)
     |  partial(func, *args, **keywords) - new function with partial application
     |  of the given arguments and keywords.




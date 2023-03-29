# Exercise No. 81


Using the built-in module *functools* and the *partial* class create from the following function:


    def mul(x, y):
        return x * y


two functions named:

-   *double*

-   *triple*

which will respectively double and triple the passed argument (functions take only one argument).

Only implement these functions.


**Tip:**


    >>> help(functools.partial)
     
    Help on class partial in module functools:
     
    class partial(builtins.object)
     |  partial(func, *args, **keywords) - new function with partial application
     |  of the given arguments and keywords.
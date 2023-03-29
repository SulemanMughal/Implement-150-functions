from functools import partial
    
    
def mul(x, y):
    return x * y
    
    
double = partial(mul, y=2)
triple = partial(mul, y=3)
from functools import partial
    
    
def power(x, y):
    return x ** y
    
    
square = partial(power, y=2)
cube = partial(power, y=3)
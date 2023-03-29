from math import factorial
    
    
def pascal_triangle(row):
    result = []
    for i in range(row + 1):
        factor = factorial(row) // (factorial(i) * factorial(row - i))
        result.append(factor)
    return result
# Solution 1

from itertools import groupby
    
    
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, len(list(group))))
    result = [''.join((i, '.' * j)) for i, j in result]
    return ''.join(result)


# Solution 2
from itertools import groupby
    
    
def compress(number):
    result = [''.join((key, '.' * len(list(group)))) for key, group in groupby(str(number))]
    return ''.join(result)
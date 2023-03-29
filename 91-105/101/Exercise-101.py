# Solution 1

from itertools import groupby
    
    
def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


# Solution 2
from itertools import groupby
    
    
def compress(number):
    result = [''.join((key, str(len(list(group))))) for key, group in groupby(str(number))]
    return '_'.join(result)
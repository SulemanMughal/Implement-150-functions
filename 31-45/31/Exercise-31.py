# Solution

def preprocess(stream):
    result = []
    for tup in stream:
        if len(tup) > 1:
            result.append(tup)
    return result


# Solution 
def preprocess(stream):
    return [tup for tup in stream if len(tup) > 1]
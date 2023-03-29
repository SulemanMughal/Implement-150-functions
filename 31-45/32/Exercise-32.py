# Solution 1

def preprocess(stream):
    result = []
    for tup in stream:
        if not all(item == None for item in tup):
            result.append(tup)
    return result


def preprocess(stream):
    return [
        tup
        for tup in stream
        if not all(item == None for item in tup)
    ]
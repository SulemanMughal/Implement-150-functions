# Solution 1

def flatten(stream):
    result = []
    for nested in stream:
        for item in nested:
            result.append(item)
    return '#' + ' #'.join(result)


# Solution 2
def flatten(stream):
    return '#' + ' #'.join([
        item
        for nested in stream
        for item in nested
    ])
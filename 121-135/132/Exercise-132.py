def reduce(function, iterable):
    if len(iterable) == 0:
        return None
    result = iterable[0]
    for item in iterable[1:]:
        result = function(result, item)
    return result
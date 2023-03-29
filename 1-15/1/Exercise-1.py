def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)
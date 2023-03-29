def is_all_equal(iterator):
    return len(set(iterator)) <= 1

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)

def is_all_equal(iterator):
    return len(set(iterator)) <= 1

def is_valid_array(array):
    if is_nested(array):
        if is_all_equal(len(row) for row in array):
            return True
    return False

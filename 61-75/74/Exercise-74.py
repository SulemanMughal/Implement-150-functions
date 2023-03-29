def trace(array):
    total = 0
    for idx, item in enumerate(array):
        total += item[idx]
    return total
def identity(n):
    array = [[0]*n for i in range(n)]
    for idx, item in enumerate(array):
        item[idx] = 1
    return array
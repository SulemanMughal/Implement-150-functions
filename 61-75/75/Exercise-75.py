def transpose(array):
    width = len(array[0])
    result = []
    
    for i in range(width):
        pair = []
        for item in array:
            pair.append(item[i])
        result.append(pair)
    return result
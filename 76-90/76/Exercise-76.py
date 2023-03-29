def max_prob(array):
    result = []
    
    for item in array:
        max_val = max(item)
        for idx, val in enumerate(item):
            if val == max_val:
                result.append([val])
    return result
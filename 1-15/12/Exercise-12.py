def concat(l1, l2):
    if not len(l1) == len(l2):
        raise ValueError('The given lists are not of the same length.')
    
    result = []
    for idx, item in enumerate(l1):
        result.append(l1[idx])
        result[idx].extend(l2[idx])
    return result
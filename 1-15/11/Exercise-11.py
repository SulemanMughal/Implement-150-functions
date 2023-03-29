def concat(l1, l2):
    result = []
    for idx, item in enumerate(l1):
        result.append(l1[idx])
        result[idx].extend(l2[idx])
    return result
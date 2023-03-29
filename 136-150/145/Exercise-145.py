def union_of_list(*data):
    result = set()
    for input_list in data:
        for item in input_list:
            result.add(item)
    return sorted(result)
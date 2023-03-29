def convert(data):
    result = {}
    keys = data[0].keys()
    for key in keys:
        result[key] = []
    for item in data:
        for key in keys:
            result[key].append(item[key])
    return result
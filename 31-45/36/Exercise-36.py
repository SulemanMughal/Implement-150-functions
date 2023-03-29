def convert(data):
    result = []
    for key, val in data.items():
        result.append([key] + [val])
    return result
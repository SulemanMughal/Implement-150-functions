def to_csv(**kwargs):
    headers = kwargs.keys()
    values = [str(val) for val in kwargs.values()]
    result = ','.join(headers) + '\n' + ','.join(values)
    return result
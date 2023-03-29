def to_csv(*values):
    result = ''
    for value in values:
        result += str(value) + ','
    return result[:-1]
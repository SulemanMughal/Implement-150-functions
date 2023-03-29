def transform(row):
    headers = 'open,high,low,close'.split(',')
    values = row.split(',')
    return {key: float(val) for key, val in zip(headers, values)}
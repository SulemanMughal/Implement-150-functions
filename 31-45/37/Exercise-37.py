def to_csv(data):
    result = 'temp,' + ','.join((str(i) for i in data['temp']))
    return result
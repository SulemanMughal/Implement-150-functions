def calculate(data):
    min_temp = min(data['temp'])
    max_temp = max(data['temp'])
    avg_temp = round(sum(data['temp']) / len(data['temp']), 2)
    return (min_temp, max_temp, avg_temp)
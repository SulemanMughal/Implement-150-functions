import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
    
    
def moving_avg(prices, window_size):
    moving_averages = []
    idx = 0
    
    while idx < len(prices) - window_size + 1:
        current_window = prices[idx: idx + window_size]
        window_average = round(sum(current_window) / window_size, 2)
        moving_averages.append(window_average)
        idx += 1
    
    return moving_averages
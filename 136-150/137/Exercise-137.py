import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    highs = list(map(lambda row: float(row[2]), rows))
    lows = list(map(lambda row: float(row[3]), rows))
    closes = list(map(lambda row: float(row[4]), rows))
    
    
def moving_min(prices, window_size):
    moving_mins = []
    idx = 0
    
    while idx < len(prices) - window_size + 1:
        current_window = closes[idx : idx + window_size]
        window_min = min(current_window)
        moving_mins.append(window_min)
        idx += 1
    
    return moving_mins
    
    
def calculate_support(prices, window_size, ratio=0.1):
    moving_mins = moving_min(prices, window_size)
    diffs = [high - low for high, low in zip(highs, lows)]
    supports = [
        round(value - (ratio * diff), 2)
        for value, diff in zip(moving_mins, diffs)
    ]
    return supports
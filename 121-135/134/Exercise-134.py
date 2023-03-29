import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    closes = list(map(lambda row: float(row[4]), rows))
    
    
def moving_avg(prices):
    moving_averages = []
    idx = 0
    
    while idx < len(prices) - 2:
        current_window = prices[idx: idx + 3]
        window_average = round(sum(current_window) / 3, 2)
        moving_averages.append(window_average)
        idx += 1
    
    return moving_averages
    
    
print(moving_avg(closes))
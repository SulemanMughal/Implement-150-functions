import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(
        map(lambda row: (row[0], float(row[1]), float(row[4])), rows)
    )
    
    
def find_doji(prices):
    diff = [
        (item[0], abs(round(item[2] - item[1], 2))) for item in prices
    ]
    min_diff = min(diff, key=lambda item: item[1])
    return min_diff[0]
    
    
print(find_doji(data))
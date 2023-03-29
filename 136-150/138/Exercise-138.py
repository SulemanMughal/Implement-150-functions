import csv
    
    
with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(
        map(lambda row: (row[0], float(row[2]), float(row[3])), rows)
    )
    
    
def max_min_diff(prices):
    diff = [round(item[1] - item[2], 2) for item in prices]
    return diff
    
    
print(max_min_diff(data))
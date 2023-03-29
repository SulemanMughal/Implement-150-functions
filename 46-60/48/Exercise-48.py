def preprocess():
    with open('data.csv', 'r') as file:
        content = [row.strip().split(',') for row in file.readlines()]
        result = [[item.strip() for item in row] for row in content]
    return result
 
 
def calculate_mean_age():    
    content = preprocess()
    ages = [int(row[3]) for row in content[1:]]
    mean = round(sum(ages) / len(ages))
    return mean
from collections import Counter
    
    
def preprocess():
    with open('data.csv', 'r') as file:
        content = [row.strip().split(',') for row in file.readlines()]
        result = [[item.strip() for item in row] for row in content]
    return result
    
    
def all_technology():    
    content = preprocess()
    names = [row[1] for row in content[1:] if row[6] == 'Technology']
    return names
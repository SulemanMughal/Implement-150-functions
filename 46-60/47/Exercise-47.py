def preprocess():
    with open('data.csv', 'r') as file:
        content = [row.strip().split(',') for row in file.readlines()]
        result = [[item.strip() for item in row] for row in content]
    return result
    
    
def get_unique_countries():
    content = preprocess()
    countries = sorted(set([row[4] for row in content[1:]]))
    return countries
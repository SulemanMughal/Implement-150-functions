from collections import Counter
    
    
def preprocess():
    with open('data.csv', 'r') as file:
        content = [row.strip().split(',') for row in file.readlines()]
        result = [[item.strip() for item in row] for row in content]
    return result
    
    
def get_top3():    
    content = preprocess()
    industries = [row[6] for row in content[1:]]
    top3 = Counter(industries).most_common(3)
    return top3
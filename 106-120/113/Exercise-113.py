import json
    
    
def json_to_csv():
    # Extract data
    with open('users.json', 'r') as file:
        content = json.load(file)
    
    # Transform data
    headers = ','.join(content[0].keys())
    users = [user.values() for user in content]
    rows = [','.join([str(item) for item in user]) for user in users]
    
    # Load data
    with open('users.csv', 'w') as file:
        file.write(headers + '\n')
        for row in rows:
            file.write(row + '\n')
import json
    
    
def filter_active_users():
    # Extract data
    with open('users.json', 'r') as file:
        content = json.load(file)
    
    # Transform data
    active = [user for user in content if user['is_active']]
    
    # Load data
    with open('active_users.json', 'w') as file:
        json.dump(active, file, indent=2)
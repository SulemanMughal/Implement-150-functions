from collections import namedtuple
import json
    
    
def json_to_object():
    # Extract data
    with open('users.json', 'r') as file:
        content = json.load(file)
    
    # Extract all the attribute names
    attributes = tuple(content[0].keys())
    
    # Create a User class
    User = namedtuple('User', attributes)
    
    # Create and return instances of the User class
    values = [tuple(user.values()) for user in content]
    users = [User(*user) for user in values]
    return users
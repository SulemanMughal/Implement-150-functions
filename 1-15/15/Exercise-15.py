# Solution 1

def filter_users(user_data):
    return [user for user in user_data if 'level' in user]


# Solution 2
def filter_users(user_data):
    return list(filter(lambda user: 'level' in user.keys(), user_data))
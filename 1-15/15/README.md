# Exercise No. 15

Define a function called `filter_users()` that takes as an argument a nested list with the given structure:


    user_data = [
        {'user_id': '3546', 'level': 64, 'is_active': True},
        {'user_id': '3467', 'level': 34, 'is_active': False},
        {'user_id': '6673', 'is_active': True},
        {'user_id': '8454', 'level': 1, 'is_active': False},
        {'user_id': '3757', 'level': 63, 'is_active': True},
        {'user_id': '1668', 'is_active': False},
    ]


And it only extracts dictionaries where there is a key named `'level'`.


**Expected result:**


    [{'is_active': True, 'level': 64, 'user_id': '3546'},
     {'is_active': False, 'level': 34, 'user_id': '3467'},
     {'is_active': False, 'level': 1, 'user_id': '8454'},
     {'is_active': True, 'level': 63, 'user_id': '3757'}]


**Example:**


    [IN]: filter_users(user_data)
    [OUT]: [{'is_active': True, 'level': 64, 'user_id': '3546'},
     {'is_active': False, 'level': 34, 'user_id': '3467'},
     {'is_active': False, 'level': 1, 'user_id': '8454'},
     {'is_active': True, 'level': 63, 'user_id': '3757'}]


**Note!** You only need to define the function.
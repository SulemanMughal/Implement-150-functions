# Exercise No. 10


Define a function called `convert()` that takes a list of dictionaries as follows:


    data = [
        {'user': 'joe', 'main_technology': 'python'},
        {'user': 'tom', 'main_technology': 'c/cpp'},
        {'user': 'michael', 'main_technology': 'cloud'},
        {'user': 'bob', 'main_technology': 'php'},
        {'user': 'lil', 'main_technology': 'html'},
        {'user': 'alice', 'main_technology': 'sql'},
    ]


And it returns a dictionary that groups items by keys (see below).


**Example:**


    [IN]: convert(data)
    [OUT]: {'main_technology': ['python', 'c/cpp', 'cloud', 'php', 'html', 'sql'], 'user': ['joe', 'tom', 'michael', 'bob', 'lil', 'alice']}


**Note!** You only need to define the function.
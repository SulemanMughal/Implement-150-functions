# Exercise No. 36

Suppose you are acquiring a data stream of the following form:


    data = {
        'device_id': '3057304985',
        'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
        'city': 'Warsaw',
        'country': 'Poland'
    }


Define a function called `convert()` that takes dictionaries of the above form as an argument and converts them to nested lists of the following form:


    [['device_id', '3057304985'],
     ['temp', [23.5, 22.0, 23.1, 25.5, 24.1]],
     ['city', 'Warsaw'],
     ['country', 'Poland']]


**Example:**


    [IN]: calculate(data)
    [OUT]: [['device_id', '3057304985'],
     ['temp', [23.5, 22.0, 23.1, 25.5, 24.1]],
     ['city', 'Warsaw'],
     ['country', 'Poland']]


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
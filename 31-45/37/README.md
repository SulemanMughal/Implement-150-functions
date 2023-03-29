# Exercise No. 37

Suppose you are acquiring a data stream of the following form:


    data = {
        'device_id': '3057304985',
        'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
        'city': 'Warsaw',
        'country': 'Poland'
    }


Define a function called `to_csv(),` which takes the dictionaries of the above form as an argument and returns temperature data in CSV format:


    'temp,23.5,22.0,23.1,25.5,24.1'


**Example:**


    [IN]: to_csv(data)
    [OUT]: 'temp,23.5,22.0,23.1,25.5,24.1'


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
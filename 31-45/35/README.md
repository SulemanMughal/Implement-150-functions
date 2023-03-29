# Exercise No. 35

Suppose you are acquiring a data stream of the following form:


    data = {
        'device_id': '3057304985',
        'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
        'city': 'Warsaw',
        'country': 'Poland'
    }


Define a function called `calculate()`, which takes the dictionaries of the above form as an argument and returns the following statistics:

-   minimum temperature
-   maximum temperature
-   average temperature - round the result to two decimal places


**Example:**


    [IN]: calculate(data)
    [OUT]: (22.0, 25.5, 23.64)


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
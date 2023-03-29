# Exercise No. 150

The following `slope()` function is given:


    def slope(point1, point2):
        numerator = point2[1] - point1[1]
        denominator = point2[0] - point1[0]
        slope = numerator / denominator
        return slope


which, based on two points calculates the slope of the line (y = ax + b) passing through these two points.


The `validate_point()` function is also given:


    def validate_point(point):
        if not isinstance(point, (tuple, list)):
            raise TypeError('Point must be a tuple or a list.')
        if not len(point) == 2:
            raise ValueError('Point must consist of two values.')
        return True


which does some input validation (helper function for `slope()`). Note that you can pass any two-element tuples or lists to our helper function to get them validated correctly. In the case of points, we will only be interested in numbers, i.e. values of type int or float. Currently calling `validate_point([4, 'py'])` is undergoing a validation process. Correct the implementation of the validate_point() function so that it checks if the values passed are of type int or float. Otherwise, raise the TypeError.


**Examples:**


    [IN]: validate_point([4, 5])
    [OUT]: True


    [IN]: validate_point({4, 5})
    [OUT]: TypeError: Point must be a tuple or a list.


    [IN]: validate_point([4, 5, 5])
    [OUT]: ValueError: Point must consist of two values.


    [IN]: validate_point([4, '5'])
    [OUT]: TypeError: Value must be of type int or float.


**Note!** You only need to define the function. You don't need to modify the `slope()` function.



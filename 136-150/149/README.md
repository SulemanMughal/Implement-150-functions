# Exercise No. 149


The following `slope()` function is given:


    def slope(point1, point2):
        numerator = point2[1] - point1[1]
        denominator = point2[0] - point1[0]
        slope = numerator / denominator
        return slope


which, based on two points calculates the slope of the line (y = ax + b) passing through these two points. The provided implementation does not include validation of the input data. Define a function called `validate_point()` that will validate a single point. Check if:

-   point is a tuple or list object, otherwise raise a TypeError

-   point consists of exactly two coordinates, otherwise raise ValueError


**Examples:**


    [IN]: validate_point([4, 5])
    [OUT]: True


    [IN]: validate_point({4, 5})
    [OUT]: TypeError: Point must be a tuple or a list.


    [IN]: validate_point([4, 5, 5])
    [OUT]: ValueError: Point must consist of two values.


**Note!** You only need to define the function. You don't need to modify the slope() function.
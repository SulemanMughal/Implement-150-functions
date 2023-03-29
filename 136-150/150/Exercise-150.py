def slope(point1, point2):
    numerator = point2[1] - point1[1]
    denominator = point2[0] - point1[0]
    slope = numerator / denominator
    return slope
    
    
def validate_point(point):
    if not isinstance(point, (tuple, list)):
        raise TypeError('Point must be a tuple or a list.')
    if not len(point) == 2:
        raise ValueError('Point must consist of two values.')
    for value in point:
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be of type int or float.')
    return True
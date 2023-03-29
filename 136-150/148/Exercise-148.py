def slope(point1, point2):
    numerator = point2[1] - point1[1]
    denominator = point2[0] - point1[0]
    slope = numerator / denominator
    return slope
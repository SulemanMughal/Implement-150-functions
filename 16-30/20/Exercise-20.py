def distance(list1, list2):
    start = 0
    for num1, num2 in zip(list1, list2):
        distance = abs(num1 - num2)
        if distance > start:
            start = distance
    return start
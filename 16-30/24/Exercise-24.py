def count(numbers):
    positive, negative = 0, 0
    for num in numbers:
        if num >= 0:
            positive += 1
        else:
            negative += 1
    return positive, negative
def remove_repetitive(numbers):
    return [
        num
        for num in numbers
        if len(set(str(num))) == len(str(num))
    ]
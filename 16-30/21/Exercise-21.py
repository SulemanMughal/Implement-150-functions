# Solution 1

def calculate(numbers):
    result = []
    for num in numbers:
        if num % 2 != 0:
            result.append(2 * num)
        else:
            result.append(num)
    return result

# Solution 2
def calculate(numbers):
    return [(2 * i if i % 2 != 0 else i) for i in numbers]
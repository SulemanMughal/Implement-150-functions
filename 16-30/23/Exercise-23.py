# Solution 1

def replace_neg(numbers):
    result = []
    for num in numbers:
        if num >= 0:
            result.append(num)
        else:
            result.append(0)
    return result

# Solution 2
def replace_neg(numbers):
    return [num if num >= 0 else 0 for num in numbers]

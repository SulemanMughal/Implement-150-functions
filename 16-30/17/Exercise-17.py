def calculate(numbers, k=5):
    result = []
    for idx in range(1, len(numbers) - 1):
        if abs(numbers[idx - 1] - numbers[idx]) >= k \
            and abs(numbers[idx + 1] - numbers[idx]) >= k:
            result.append(numbers[idx])
    return result  
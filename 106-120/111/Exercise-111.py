def binary_to_int():
    with open('binary.txt', 'r') as file:
        content = file.read().split()
    numbers = [int('0b' + number, base=2) for number in content]
    return numbers
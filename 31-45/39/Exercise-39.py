def collatz(num):
    count = 0
    while num != 1:
        if num % 2 == 1:
            num = num * 3 + 1
        else: 
            num = num / 2
        count += 1
    return count
# Solution 1


def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
    
    
def calculate():
    return [i for i in range(100, 1000) if is_palindrome(i)]
    
    
print(calculate())


# Solution 2

def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]
    
    
def calculate():
    return list(filter(is_palindrome, [i for i in range(100, 1000)]))
    
    
print(calculate())
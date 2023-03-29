# Solution 1

def is_palindrome(string):
    inverse = string[::-1]
    if string == inverse:
        return True
    else:
        return False
    

# Solution 2
def is_palindrome(string):
    inverse = string[::-1]
    return True if string == inverse else False
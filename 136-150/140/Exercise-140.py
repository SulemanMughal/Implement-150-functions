class EmptyStackError(Exception):
    pass
    
    
class Stack:
    """The simplest stack."""
    
    def __init__(self):
        self._data = []
    
    def __len__(self):
        return len(self._data)
    
    def push(self, item):
        self._data.append(item)
    
    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()
    
    def is_empty(self):
        return len(self._data) == 0
    
    
def is_palindrome(string):
    stack = Stack()
    is_palindrome_flag = True
    
    for char in string:
        stack.push(char)
    
    for char in string:
        if not char == stack.pop():
            is_palindrome_flag = False
    
    return is_palindrome_flag
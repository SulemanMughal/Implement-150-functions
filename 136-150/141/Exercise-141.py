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
    
    def top(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data[-1]
    
    
def is_valid_expression(expression):
    left_side = '([{'
    right_side = ')]}'
    
    stack = Stack()
    
    for char in expression:
        if char in left_side:
            stack.push(char)
        elif char in right_side:
            if stack.is_empty():
                return False
            if right_side.index(char) != left_side.index(stack.pop()):
                return False
    return stack.is_empty()
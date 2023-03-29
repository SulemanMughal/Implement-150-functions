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
    
    
def is_valid_html(html):
    stack = Stack()
    first_char_idx = html.find('<')
    while first_char_idx != -1:
        next_char_idx = html.find('>', first_char_idx + 1)
        if next_char_idx == -1:
            return False
        tag = html[first_char_idx + 1: next_char_idx]
        if not tag.startswith('/'):
            stack.push(tag)
        else:
            if stack.is_empty():
                return False
            if tag[1:] != stack.pop():
                return False
        first_char_idx = html.find('<', next_char_idx + 1)
    return stack.is_empty()
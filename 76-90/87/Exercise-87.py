def stick(*args):
    args = [arg for arg in args if isinstance(arg, str)]
    result = '#'.join(args)
    return result
    
    
print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))
def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]
    
    
def bitwise_xor(a, b):
    if a < 0 or b < 0:
        raise ValueError('Both numbers must be positive.')
    
    a_bin = decimal_to_binary(a)
    b_bin = decimal_to_binary(b)
    
    max_length = max(len(a_bin), len(b_bin))
    
    a_zfill = a_bin.zfill(max_length)
    b_zfill = b_bin.zfill(max_length)
    
    binary_xor = [
        str(int(char_a != char_b))
        for char_a, char_b in zip(a_zfill, b_zfill)
    ]
    
    binary_result = ''.join(binary_xor)
    decimal_result = int(binary_result, base=2)
    
    return decimal_result
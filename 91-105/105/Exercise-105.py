# Solution 1


def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance
    
    
def hamming_weight(u):
    zero_vector = '0' * len(u)
    return hamming_distance(u, zero_vector)



# Solution 2
def hamming_distance(u, v):
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    distance = 0
    for i in range(len(u)):
        if u[i] != v[i]:
            distance += 1
    return distance
    
    
def hamming_weight(u):
    return u.count('1')
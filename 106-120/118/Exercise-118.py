def lev(a, b):
    
    if len(b) == 0:
        return len(a)
    
    if len(a) == 0:
        return len(b)
    
    if a[0] == b[0]:
        return lev(a[1:], b[1:])
    
    residual = 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))
    return residual
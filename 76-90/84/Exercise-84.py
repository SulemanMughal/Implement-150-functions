def fv(pv, rate, n, m=1):
    return round(pv * (1 + (rate / m)) ** (n * m), 2)
    
    
print(fv(1000, 0.04, 1))
print(fv(1000, 0.04, 1, 2))
print(fv(1000, 0.04, 1, 4))
print(fv(1000, 0.04, 1, 12))
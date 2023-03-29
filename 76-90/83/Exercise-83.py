def fv(pv, rate, n):
    return round(pv * (1 + rate) ** n, 2)
    
    
print(fv(1000, 0.04, 1))
print(fv(1000, 0.04, 2))
print(fv(1000, 0.03, 5))
print(fv(10000, 0.09, 10))
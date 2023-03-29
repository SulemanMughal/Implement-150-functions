from functools import partial
    
    
def fv(rate, m, n, pv):
    return pv * (1 + (rate / m)) ** (n * m)
    
    
annual_acc_factor = partial(fv, n=1, pv=1)
    
print(annual_acc_factor(0.04, 1))
print(annual_acc_factor(0.04, 4))
print(annual_acc_factor(0.06, 12))
from functools import partial
    
    
def fv(rate, m, n, pv):
    return pv * (1 + (rate / m)) ** (n * m)
    
    
annual_acc_factor = partial(fv, n=1, pv=1)
    
annual_acc_factor_4 = partial(annual_acc_factor, m=4)
annual_acc_factor_12 = partial(annual_acc_factor, m=12)
    
print(annual_acc_factor_4(0.04))
print(annual_acc_factor_12(0.06))
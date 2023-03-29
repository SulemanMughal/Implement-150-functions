# Exercise No. 85

Consider the compound capitalization model, where:

-   *pv* - is the present value of the investment

-   *r* - interest rate (annual)

-   *n* - the number of years of investment

-   *m* - number of capitalization periods during the year (default 1)

A function `fv()` was implemented to calculate the future value of investment depending on the number of capitalization periods during the year (m parameter, default 1):


    def fv(pv, rate, n, m=1):
        return round(pv * (1 + (rate / m)) ** (n * m), 2)


Using the built-in functools module, the class partial and the `fv()` function create the function `annual_acc_factor()`, which calculates the annual accumulation factor.

In response, print value of the annual accumulation factor for the following cases:

-   4% (annual) interest rate and annual capitalization

-   4% (annual) interest rate and quarterly capitalization

-   6% interest rate (annual) and monthly capitalization


**Expected result:**


    1.04
    1.04060401
    1.0616778118644983



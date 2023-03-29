# Exercise No. 86

Consider the compound capitalization model, where:

-   *pv* - is the present value of the investment

-   *r* - interest rate (annual)

-   *n* - the number of years of investment

-   *m* - number of capitalization periods during the year (default 1)

A function `fv()` was implemented to calculate the future value of investment depending on the number of capitalization periods during the year (*m* parameter, default 1):


    def fv(pv, rate, n, m=1):
        return round(pv * (1 + (rate / m)) ** (n * m), 2)


The `annual_acc_factor()` function was created, which calculates the annual accumulation factor:


    annual_acc_factor = partial(fv, n=1, pv=1)


Create two more functions that calculates the value of the annual accumulation factor for the following capitalization models:

-   *quarterly* -> function name annual_acc_factor_4

-   *monthly* -> function name annual_acc_factor_12

In response, print the value of the annual accumulation factor for:

-   quarterly capitalization and an interest rate of 4% (annually)

-   monthly capitalization and an interest rate of 6% (annually)


**Expected result:**


    1.04060401
    1.0616778118644983
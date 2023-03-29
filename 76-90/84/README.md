# Exercise No. 84


Consider the compound capitalization model, where:

-   *pv* - is the present value of the investment

-   *r* - interest rate (annual)

-   *n - the number of years of investment

-   *m* - number of capitalization periods during the year (default 1)

Implement `fv()` function that calculates the future value of investment. Take into account the number of capitalization periods (*m* parameter) per year. Round the result to two decimal places.

In response, print the future values of investment for the following cases:

-   `pv=1000, r=0.04, n=1- annual capitalization`

-   `pv=1000, r=0.04, n=1, m=2- semi-annual capitalization`

-   `pv=1000, r=0.04, n=1. m=4- quarter capitalization`

-   `pv=1000, r=0.04, n=1, m=12- monthly capitalization`


**Expected result:**


    1040.0
    1040.4
    1040.6
    1040.74



# Exercise No. 137

The cdr.csv file is attached to the exercise. The file contains the quotations of CD Projekt S. A. company for March 2021:


    Date,Open,High,Low,Close,Volume
    2021-03-01,237.4,241,225.2,240.3,1089101
    2021-03-02,240.9,245.9,236,241.3,674141
    2021-03-03,241.8,245.3,227,228.3,836642
    ...


Explanations:

-   Date - session date

-   Open - share price at the open of the session

-   High - the highest share price during the session

-   Low - the lowest share price during the session

-   Close - share price at the close of the session

-   Volume - trading volume


The cdr.csv file has been loaded.

We want to set some levels of support for the price. For example, a 3-day rolling minimum for moves per session, a 10-day rolling minimum for short-term moves, etc. A function called `moving_min()` has been implemented for this, which returns a list with values for the rolling minimum.

However, we want to maintain an additional level of security for the support levels and move slightly away from the price levels at which the transactions took place. Implement a function called `calculate_support()` that calculates the support levels for the price according to the formula described below:


    moving support level = n-period moving minimum - difference * ratio


Where the difference is the difference between the highest value of the share price and the lowest value on a given trading day. The ratio determines the significance of the difference itself.

The `calculate_support()` function takes three arguments:

-   prices - list of prices

-   window_size - the number of periods for which we calculate the support

-   ratio - default 0.1


**Example:**


    [IN]: calculate_support(closes, 10)
    [OUT]: [208.62, 209.21, 208.37, 209.05, 209.3, 209.65, 209.13, 208.55, 215.3, 206.62, 207.19, 207.14, 207.21, 189.4]


**Example:**


    [IN]: calculate_support(closes, 10, 0.5)
    [OUT]: [202.3, 205.25, 201.05, 204.45, 205.7, 207.45, 204.85, 201.95, 208.5, 200.7, 203.55, 203.3, 203.65, 185.0]



You just need to implement the `calculate_support()` function. The tests run several test cases to validate the solution.
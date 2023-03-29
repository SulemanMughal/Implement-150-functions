# Exercise No. 136

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


The cdr.csv file has been loaded. All closing prices have been extracted as a list and assigned to the variable closes:


    [240.3, 241.3, 228.3, 235.0, 232.0, 232.0, 223.0, 210.2, 221.0, 226.5, 229.9, 229.5, 231.0, 220.7, 223.2, 217.0, 220.7, 217.1, 208.1, 212.0, 239.7, 217.9, 190.5]


We want to set some support levels for the price and for that we need a rolling minimum. For example, a 3-day rolling minimum for moves per session, a 10-day rolling minimum for short-term moves, etc. Try to implement a function called `moving_min()` that takes two arguments:

-   prices - list of prices for the calculation of the rolling minimum

-   window_size - the number of periods for which we calculate the rolling minimum (for example window_size = 15 is a 15-day rolling minimum)

and returns a list with values for the rolling minimum.


**Example:**


    [IN]: moving_min(closes, 3)
    [OUT]: [228.3, 228.3, 228.3, 232.0, 223.0, 210.2, 210.2, 210.2, 221.0, 226.5, 229.5, 220.7, 220.7, 217.0, 217.0, 217.0, 208.1, 208.1, 208.1, 212.0, 190.5]


**Example:**


    [IN]: moving_min(closes, 10)
    [OUT]: [210.2, 210.2, 210.2, 210.2, 210.2, 210.2, 210.2, 210.2, 217.0, 208.1, 208.1, 208.1, 208.1, 190.5]


You just need to implement the `moving_min()` function. The tests run several test cases to validate the solution.
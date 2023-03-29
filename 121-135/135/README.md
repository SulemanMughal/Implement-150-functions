# Exercise No. 135

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


We want to calculate the n-period moving average for the price. To do this, implement a function called `moving_avg()` that takes two arguments:

-   prices - list of prices for the calculation of the moving average

-   window_size - the number of periods for which we calculate the moving average (for example window_size = 15 is a 15-day moving average)

and returns a list with the values for the moving average (each average value rounded to two decimal places).

Please note that a moving average list (result) is n - 1 items shorter than a list with prices.


**Example:**


    [IN]: moving_avg(closes, 8)
    [OUT]: [230.26, 227.85, 226.0, 226.2, 225.51, 225.39, 223.98, 224.0, 224.85, 224.81, 223.64, 220.91, 218.72, 219.81, 219.46, 215.38]


**Example:**


    [IN]: moving_avg(closes, 15)
    [OUT]: [228.26, 226.71, 225.33, 224.59, 222.79, 221.46, 221.97, 221.63, 220.32]


You just need to implement the `moving_avg()` function. The tests run several test cases to validate the solution.
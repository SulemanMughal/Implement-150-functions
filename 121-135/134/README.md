# Exercise No. 134

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

Financial instrument quotes are often presented as candlestick charts. All the above information is used to build candlestick charts.

Wiki: https://en.wikipedia.org/wiki/Candlestick_chart

Load the cdr.csv file. You can use the built-in csv module for this. Extract all closing prices as a list and assign to the variable closes:


    [240.3, 241.3, 228.3, 235.0, 232.0, 232.0, 223.0, 210.2, 221.0, 226.5, 229.9, 229.5, 231.0, 220.7, 223.2, 217.0, 220.7, 217.1, 208.1, 212.0, 239.7, 217.9, 190.5]


We want to calculate the 3-day moving average for the close price. Try to implement a function called `moving_avg()`, which takes a list of closing prices as an argument and returns a list with values for a 3-day moving average (round the values to two decimal places). Please note that the number of items in the 3-day moving average list is less than the number with closing prices by 2 items.


In response, call `moving_avg()` function and print the result to the console.


**Expected result:**


    [236.63, 234.87, 231.77, 233.0, 229.0, 221.73, 218.07, 219.23, 225.8, 228.63, 230.13, 227.07, 224.97, 220.3, 220.3, 218.27, 215.3, 212.4, 219.93, 223.2, 216.03]



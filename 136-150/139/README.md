# Exercise No. 139

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


The cdr.csv file has been loaded as shown below:


    import csv
     
     
    with open('cdr.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        columns = next(reader)
        rows = list(reader)
        data = list(
            map(lambda row: (row[0], float(row[1]), float(row[4])), rows)
        )


We use the data variable to check the implementation of the function in this exercise.


One of the most characteristic candlestick formations is the doji. A doji pattern is a market situation in which the opening and closing prices are the same or close to each other.

We want to write a function called `find_doji()` which finds the date of the daily candle closest to the doji patern of CD Projekt's quotes for March 2021. To this end, we will introduce the concept of a candle body. The body of the candle is the distance from the opening price to the closing price. To find the candle closest to the doji, find the candle with the smallest body.


In response, call `find_doji()` function on the data list and print the result to the console.


**Expected result:**


    [IN]: find_doji(data)
    [OUT]: '2021-03-02'
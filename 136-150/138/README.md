# Exercise No. 138

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
        data = list(map(lambda row: (row[0], float(row[2]), float(row[3])), rows))


We want to determine the height of a single candle (one session) calculated as the distance from the highest to the lowest price. To do this, implement a function called `max_min_diff()` that returns the calculated distances. Use the data variable for calculations.

In response, call the `max_min_diff()` function and print the result to the console.


**Expected result:**


    [IN]: max_min_diff(data)
    [OUT]: [15.8, 9.9, 18.3, 11.5, 9.0, 5.5, 10.7, 16.5, 17.0, 14.8, 9.1, 9.6, 8.9, 11.0, 9.1, 4.2, 9.6, 7.3, 13.8, 7.4, 27.5, 34.8, 22.2]



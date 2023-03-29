# Exercise No. 46


The data.csv file is attached to this exercise, containing basic data about the richest people in the world. Define a function called `preprocess()` that will read the given file and return the data as nested lists (see below):


**Function call:**


    [IN]: preprocess()
    [OUT]: [['Rank', 'Name', 'Networth', 'Age', 'Country', 'Source', 'Industry'],
     ['1', 'Elon Musk', '219', '50', 'United States', 'Tesla', 'Automotive'],
     ['2', 'Jeff Bezos', '171', '58', 'United States', 'Amazon', 'Technology'],
     ['3',
      'Bernard Arnault & family',
      '158',
      '73',
      'France',
      'LVMH',
      'Fashion & Retail'],
     ['4', 'Bill Gates', '129', '66', 'United States', 'Microsoft', 'Technology'],
    ...


Pay attention to getting rid of whitespace characters (unnecessary spaces, newlines).


**Note!** You only need to define the function.
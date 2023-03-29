# Exercise No. 18


Define a function called `calculate()` that takes a sentence as an argument. For the sake of simplicity, we assume that the sentence doesn't contain punctuation marks and words are separated only by a space. The function is to return a list of all possible word permutations of the sentence (see below).


**Example:**


    [IN]: calculate('python is the')
    [OUT]: ['python is the',
     'python the is',
     'is python the',
     'is the python',
     'the python is',
     'the is python']


    [IN]: calculate('python is the best')
    [OUT]: ['python is the best',
     'python is best the',
     'python the is best',
     'python the best is',
     'python best is the',
     'python best the is',
     'is python the best',
     'is python best the',
     'is the python best',
     'is the best python',
     'is best python the',
     'is best the python',
     'the python is best',
     'the python best is',
     'the is python best',
     'the is best python',
     'the best python is',
     'the best is python',
     'best python is the',
     'best python the is',
     'best is python the',
     'best is the python',
     'best the python is',
     'best the is python']


**Tip!** You can use the built-in itertools module to do permutations.


**Note!** You only need to define the function.
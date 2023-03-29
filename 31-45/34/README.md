# Exercise No. 34

Define a function called `flatten()` that takes as an argument a nested tuple of lists, which consists of words (see below):


    (['apple'], ['gym', 'fit'], ['movie', 'netflix'])


The function is to process the given tuple and return one string which is a sequence of hashtags composed of the given words:


    '#apple #gym #fit #movie #netflix'


**Examples:**


    [IN]: flatten((['apple'], ['gym', 'fit'], ['movie', 'netflix']))
    [OUT]: '#apple #gym #fit #movie #netflix'


    [IN]: flatten((['orange'], [], ['movie', 'netflix']))
    [OUT]: '#orange #movie #netflix'


You don't need to implement validation in your solution.


**Note!** You only need to define the function.
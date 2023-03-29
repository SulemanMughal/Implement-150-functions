# Exercise No. 27

Define a function called `convert()` that takes English text as an argument and replaces all digits  (not numbers) in the text with words (see below):


    'you need to have 2 tickets' -> 'you need to have two tickets'
    '3 tickets cost 15 euro' -> 'three tickets cost 15 euro'
    '3 tickets cost 5 Euro' -> 'three tickets cost five euro


You don't need to implement validation in your solution. Notice that the number 15 has not been changed (only digits).


**Example:**


    [IN]: convert('you need to have 2 tickets')
    [OUT]: 'you need to have two tickets'


    [IN]: convert('3 tickets cost 15 euro')
    [OUT]: 'three tickets cost 15 euro'


**Note!** You only need to define the function.
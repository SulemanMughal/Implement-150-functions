# Exercise No. 107

Consider the problem below. We have given a sequence of characters, and we want to extract from it all the substrings of length n in the order they appear in the sequence.

For example, from a sequence of characters `'python'` we can extract a 3-digit series:


    ['pyt', 'yth', 'tho', 'hon']


or 4-digit:


    ['pyth', 'ytho', 'thon']


Implement a function called `get_slices()` that takes two arguments:

-   *sequence* - the sequence of characters to be processed

-   *length* - length of the substrings to be extracted from the sequence

If the value of the length argument is less than 1, raise the *ValueError* with the message:

`'The length cannot be less than 1.'`

If the value of the *length* argument is greater than the length of the given sequence, raise the *ValueError* with the message:

`'The length cannot be greater than sequence.'`


**Example:**


    [IN]: get_slices('esmartdata', 5)
    [OUT]: ['esmar', 'smart', 'martd', 'artda', 'rtdat', 'tdata']


**Example:**


    [IN]: get_slices('654646849173', 6)
    [OUT]: ['654646', '546468', '464684', '646849', '468491', '684917', '849173']


You just need to implement the get_slices() function. The tests run several test cases to validate the solution.
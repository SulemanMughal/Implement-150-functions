# Exercise No. 120

In cryptography, a **Caesar cipher** is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the string is replaced by a letter some fixed number of positions down the alphabet.

An example of the encryption. Consider only capital letters in English (let's just call it *alphabet*):


    ABCDEFGHIJKLMNOPQRSTUVWXYZ


Shifting the above alphabet by a certain number (key = 2) gives us the cipher:


    CDEFGHIJKLMNOPQRSTUVWXYZAB


Let's put it together:


    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    CDEFGHIJKLMNOPQRSTUVWXYZAB


Note that for the last letters of the alphabet (Y, Z) the initial letters are matched.

Having an alphabet and a cipher, we can start encrypting. Consider the message below:


    'ATTACK AT DAWN!'


Using the Caesar cipher with an offset of 2 (key = 2) we get:


    'CVVCEM CV FCYP!'


Implement a function called `generate_cipher()` that takes two arguments:

-   *alphabet* - the alphabet we want to use for encryption

-   *key* - key, offset (default value 2)

and returns the alphabet in encrypted form.


**Example:**


    [IN]: import string
    [IN]: generate_cipher(string.ascii_uppercase)
    [OUT]: CDEFGHIJKLMNOPQRSTUVWXYZAB


**Example:**


    [IN]: import string
    [IN]: generate_cipher(string.ascii_uppercase, 3)
    [OUT]: DEFGHIJKLMNOPQRSTUVWXYZABC


**Example:**


    [IN]: import string
    [IN]: generate_cipher(string.ascii_lowercase, 13)
    [OUT]: nopqrstuvwxyzabcdefghijklm


You just need to implement the `generate_cipher()` function. The tests run several test cases to validate the solution.
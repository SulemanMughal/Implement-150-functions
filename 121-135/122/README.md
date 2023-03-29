# Exercise No. 122

In cryptography, a **Caesar cipher** is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the string is replaced by a letter some fixed number of positions down the alphabet.

An example of the encryption. Consider only capital letters in English (let's just call it alphabet):


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


Functions named: `generate_cipher()` and `encrypt()` have been implemented. The first generates a cipher, the second encrypts the message.

You are one of Caesar's commanders and you need to decode a message that is critical to the success of your mission. Implement a function called `decrypt()` that takes three arguments:

-   *alphabet* - the alphabet we use for encryption

-   *message* - the message we want to decrypt

-   *key* - key, offset

and decrypt the message.

In the implementation, you can use the `encrypt()` function.


**Example:**


    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'RAVJQP', 2)
    [OUT]: PYTHON


**Example:**


    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'CVVCEM CV FCYP!', 2)
    [OUT]: ATTACK AT DAWN!


**Example:**


    [IN]: import string
    [IN]: decrypt(string.ascii_uppercase, 'FGBC GUR NGGNPX!', 13)
    [OUT]: STOP THE ATTACK!


You just need to implement the `decrypt()` function. The tests run several test cases to validate the solution.
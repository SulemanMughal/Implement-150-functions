# Exercise No. 121


In cryptography, a `**Caesar cipher**` is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the string is replaced by a letter some fixed number of positions down the alphabet.

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


A function called `generate_cipher()` has been implemented that generates the Caesar cipher for the alphabet and key:


    def generate_cipher(alphabet, key=2):
        cipher = ''
        for letter in alphabet:
            new_idx = (alphabet.index(letter) + key) % len(alphabet)
            cipher += alphabet[new_idx]
        return cipher


Implement a function called `encrypt()` that takes three arguments:

    alphabet - the alphabet we want to use for encryption

    message - the message we want to encrypt

    key - key, offset

In the implementation, you can use the `generate_cipher()` function. If any character in the message is not in the alphabet, add it as it is (for example, a space or an exclamation point).


**Example:**


    [IN]: import string
    [IN]: encrypt(string.ascii_uppercase, 'PYTHON', 2)
    [OUT]: RAVJQP


**Example:**


    [IN]: import string
    [IN]: encrypt(string.ascii_uppercase, 'ATTACK AT DAWN!', 2)
    [OUT]: CVVCEM CV FCYP!


**Example:**


    [IN]: import string
    [IN]: encrypt(string.ascii_uppercase, 'STOP THE ATTACK!', 13)
    [OUT]: FGBC GUR NGGNPX!


You just need to implement the `encrypt()` function. The tests run several test cases to validate the solution.
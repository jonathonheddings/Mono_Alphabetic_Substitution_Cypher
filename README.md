# Mono-Alphabetic Substitution Message Encryption
This python program provides functions for using Mono-Alphabetic Substitution cypher on text files and messages.

---
### Overview of The Encryption    
  The Mono-alphabetic Substitution Cypher 
       This cypher works by defining a permutation on the letters in the
   alphabet and applying it to a message. Each letter in the plaintext alphabet
   corresponds to a unique letter in cyphertext alphabet (it is bijective). Decryption
   involves applying the bijection in reverse.
       The Mono-alphabetic Substitution Cypher is vulnerable to frequency analysis as 
   the frequency of each letter is presevered during the shift.     

#### Mono-Alphabetic Substitution (MAS) Encryption Function
```python
# The encryption function takes the index of the letters in the plaintext 
#   and finds its corresponding cyphertext value using the key. It takes a list as the key,
#   with values 0-25 or a dict with the alphabet and integers 1-26 as key value pairs.
def mono_encrypt(message, key):

    # Checks to see if they key needs converting
    if type(key) == dict:
        key = [(x - 1) % 26 for x in list(key.values())]

    # Loops through the text applying the substitution
    cyphertext = ''
    for letter in message:
        cyphertext += alphabet_list[key[(alphabet_dict[letter] - 1) % 26]]
    return cyphertext
```

This function when ran on a message will return an encrypted string of text. The decryption function works
in a similar way. It works by taking the index of the cyphertext letters, finding the position in the key where that letters index is located, and converting that position back into English letters, this recovers the plaintext.

Here is some test code for the MAS functions:

```python
    a = filter_plaintext('The Big Oxmox advised her not to do so, because there were thousands of bad Commas')
    key = [1,0,2,5,4,6,25,7,8,9,13,17,12,10,14,15,11,16,18,19,22,21,23,20,3,24]
    key_dict = {'a':2, 'b':1, 'c':14, 'd':4, 'e':21, 'f':6, 'g':18, 'h':26, 'i':23, 'j':13, 'k':24, 'l':11, 'm':12, 'n':17, 
                 'o':3, 'p':5, 'q':15, 'r':7, 's':25, 't':10, 'u':16, 'v':9, 'w':22, 'x':20, 'y':19, 'z':8}
    encrypted, encrypted_dict = mono_encrypt(a, key), mono_encrypt(a, key_dict)
    print('Plaintext: ', a)
    print('Using List Key: ', encrypted)
    print('Using Dict Key: ', encrypted_dict)
    print('Decrypted: ', mono_decrypt(encrypted, key))    
```
And here is the output from it:

```
Plaintext:  thebigoxmoxadvisedhernottodosobecausetherewerethousandsofbadcommas
Using List Key:  theaizoumoubfvisefheqkottofosoaecbwsetheqexeqethowsbkfsogabfcommbs
Using Dict Key:  jzuawrctlctbdiwyudzugqcjjcdcycaunbpyujzuguvugujzcpybqdycfabdncllby
Decrypted:  thebigoxmoxadvisedhernottodosobecausetherewerethousandsofbadcommas
```

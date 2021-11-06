#       #               #               #               #               #
#
#   The Mono-alphabetic Substitution Cypher 
#       This cypher works by defining a permutation on the letters in the
#   alphabet and applying it to a message. Each letter in the plaintext alphabet
#   corresponds to a unique letter in cyphertext alphabet (it is bijective). Decryption
#   involves applying the bijection in reverse.
#       The Mono-alphabetic Substitution Cypher is vulnerable to frequency analysis as 
#   the frequency of each letter is presevered during the shift.     
#       
#       #               #               #               #               #


# Defines the regular bijection from the alphabet to the positive integers mod 26
alphabet_dict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 
                 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26}
alphabet_list = list(alphabet_dict.keys())
test = 'test.txt'


# This function filters a .txt file or a string into only
#       plain lowercase text which is what
#       is required for using the cypher
def filter_plaintext(txtfile):
    filteredtext = ""
    try: # tries to open a file if the string is a filename
        with open(txtfile) as f:
            plaintext = f.readlines()
            for line in plaintext:
                for character in line.lower():
                    try:
                        number = alphabet_dict[character]
                        filteredtext += character
                    except: pass
    except: # if its not, treat it as the message
        for character in txtfile.lower():
                    try:
                        number = alphabet_dict[character]
                        filteredtext += character
                    except: pass
        return filteredtext
    return filteredtext


# The encryption function just takes the index of the letters in the plaintext 
#   and finds its corresponding cyphertext value using the key. It takes a list as the key
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


# The decryption works by taking the index of the cyphertext letters, finding
#   the position in the key where that letters index is located, and converting
#   that position back into English letters, this recovers the plaintext
def mono_decrypt(message, key):

    if type(key) == dict:
        key = [(x - 1) % 26 for x in list(key.values())]
    
    cyphertext = ''
    for letter in message:
        key_index = (alphabet_dict[letter] - 1) % 26
        for i in range(len(key) - 1):
            if key[i] == key_index:
                cyphertext += alphabet_list[i]
    return cyphertext


# This is a test. It takes an input file and runs it through the cypher and back again
if(__name__ == "__main__"):
    a = filter_plaintext('The Big Oxmox advised her not to do so, because there were thousands of bad Commas')
    key = [1,0,2,5,4,6,25,7,8,9,13,17,12,10,14,15,11,16,18,19,22,21,23,20,3,24]
    key_dict = {'a':2, 'b':1, 'c':14, 'd':4, 'e':21, 'f':6, 'g':18, 'h':26, 'i':23, 'j':13, 'k':24, 'l':11, 'm':12, 'n':17, 
                 'o':3, 'p':5, 'q':15, 'r':7, 's':25, 't':10, 'u':16, 'v':9, 'w':22, 'x':20, 'y':19, 'z':8}
    encrypted, encrypted_dict = mono_encrypt(a, key), mono_encrypt(a, key_dict)
    print('Plaintext: ', a)
    print('Using List Key: ', encrypted)
    print('Using Dict Key: ', encrypted_dict)
    print('Decrypted: ', mono_decrypt(encrypted, key))

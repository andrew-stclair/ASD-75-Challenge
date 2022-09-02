from itertools import cycle
from textwrap import wrap

atbash_substitution = {
    "A": "Z",
    "B": "Y",
    "C": "X",
    "D": "W",
    "E": "V",
    "F": "U",
    "G": "T",
    "H": "S",
    "I": "R",
    "J": "Q",
    "K": "P",
    "L": "O",
    "M": "N",
    "N": "M",
    "O": "L",
    "P": "K",
    "Q": "J",
    "R": "I",
    "S": "H",
    "T": "G",
    "U": "F",
    "V": "E",
    "W": "D",
    "X": "C",
    "Y": "B",
    "Z": "A",
    " ": " ",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9",
    "0": "0",
    ".": "."
}

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

def atbash(atbash_string: str) -> str:
    count = 0
    atbash_string = list(atbash_string)
    for index in range(len(atbash_string)):
        atbash_string[index] = atbash_substitution[atbash_string[index]]
    atbash_string = ''.join(atbash_string)
    return atbash_string

def byte_xor(ba1: bytes, ba2: bytes) -> bytes:
    return bytes([_a ^ _b for _a, _b in zip(ba1, cycle(ba2))])

def matrix(input_string: str, width: int, depth: int)  -> list:
    wrapped_string = wrap(input_string, width)
    return zip(*[iter(wrapped_string)]*depth)

def clarity(matrix: list) -> str:
    output = ''
    for part in matrix:
        prange = len(part[0])
        for i in range(prange):
            for chunk in part:
                output += chunk[i]
    return output

def clarity_matrix(input_string: str, width: int, depth: int) -> str:
    return clarity(matrix(input_string, width, depth))

def morse_encrypt(message: str) -> str:
    cipher = ''
    for letter in message:
        if letter != ' ':
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher
 
# Function to decrypt the string
# from morse to english
def morse_decrypt(message: str) -> str:
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message:
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher

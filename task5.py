import random
import math


asciicode = []
stringforascii = 'hi this will be a ascii code'
numberlist = []


asciicode = list(stringforascii)
print(asciicode)

for x in asciicode:
    asciitonumber = asciicode[x]
    if asciitonumber != ' ':
        number = ord(asciitonumber)
        numberlist = numberlist.append(number)
        
        

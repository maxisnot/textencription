
import random
import math

numkey = []
charkey = []
x = 0
while x != 8:
    randomint = random.randint(33,126)
    ascii = chr(randomint)
    numkey.append(randomint)
    charkey.append(ascii)
    x = x + 1
charkeySTRING = ''.join(charkey)
print('your key is:  \n {0}'.format(charkeySTRING))

x = 0
total = 0
while x != 8:
    numkeyMath = numkey[x]
    x=x+1
    total = numkeyMath + total


total = total/8
total = math.trunc(total)
total = total - 32
print(total)


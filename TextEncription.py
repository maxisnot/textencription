# Date 8/2/2022
import random


def main(words):

    ValuesForYes = ['y','yes','Y','Yes']
    
    print('would you like to encript')
    encript = input('yes or no \n - ')
    if encript == ValuesForYes:
        print(Encription(words))
    else:
        print('would you like to decript')
        decript = input('yes or no \n - ')
        if decript == ValuesForYes:
            print(Decription())
        else:
            print('push enter to exit program \n -')
            exit(input())
    
            

def Encription(words):
    WhatNeedsToEncript = input('name the flle that needs encription')
    encriptFile = open(WhatNeedsToEncript,'r')

    random.randint(33, 126)

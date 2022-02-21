import random
a = 1
while a != 8:
    apendment = random.randint(33,126)
    print(apendment)
    a += 1

    # to convert ascii code to character 
    # use "chr()" function with acsii value as parameter to function


    asc = [x for x in range(65, 65+26)] 
    #asc store ascii value form "A" to "Z"
    string = ""
    for i in asc:
      string += chr(i)
      
    print(string) #converted list of ascii code to string

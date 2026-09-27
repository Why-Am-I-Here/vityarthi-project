import random

from assets import *

from end import *

#Working and Recursing of the code:

while True:
    startCode = int(input("Press 1 to Encrypt and 2 to Decrypt: "))
#    encryptions = int(input("Enter the number of encyrptions: ")) - for future project
    if startCode == 1:
        inpEnc = str(input("Enter your string to Encrypt: "))
        final = encrypt(inpEnc)
        print(final)
    elif startCode == 2:
        inpDec = str(input("Enter your string to Decode: "))
        final = decrypt(inpDec)
        print(final)
    else:
        break
    
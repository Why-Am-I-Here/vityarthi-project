from random import *
from assets import *
from sf import *
from rvrm import *

# Encrypt

def encrypt(x):
    sF = reverse(sliceFront(x))
    sB = reverse(sliceBack(x))
    RA1 = "".join([str(random.choice(alphabets)) for i in range(4)])
    RA2 = "".join([str(random.choice(alphabets)) for i in range(4)])
    RN = "".join([str(random.choice(numbers)) for i in range(4)])
    final = RA1 + sF + RN + sB + RA2
    return final

# Decrypt 

def decrypt(x):
    y = remove(x)
    z = finalSlice(y)
    return z

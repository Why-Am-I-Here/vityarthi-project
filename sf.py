from rvrm import *

# Slice:

def sliceFront(x):
    if len(x)%2==0:
        l = int(len(x)/2)
        j = x[:l]
    else:
        l = int(len(x)/2 + 0.5)
        j = x[:l]
    return j

def sliceBack(x):
    if len(x)%2==0:
        l = int(len(x)/2)
        j = str(x[l:len(x)])
    else:
        l = int(len(x)/2 + 0.5)
        j = str(x[l:len(x)])
    return j

def finalSlice(x):
    l = len(x) - 4
    if l%2==0:
        l1 = l//2
    else:
        l1 = l//2 + 0.5
    x1 = x[0:l1]
    x2 = x[l1+4:]
    final = "".join(reverse(x1)) + "".join(reverse(x2))
    return final
    

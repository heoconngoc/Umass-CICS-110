# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def nand (A, B):
    if (A == True and B == True):
        return False
    else:
        return True
# print(nand(True, True))  
# print(nand(False, True)) 

def implies (A, B):
    if (A == True and B == False):
        return False
    else:
        return True
# print(implies(True, True))
# print(implies(True, False)) 

def iff (A, B):
    if ((A == True and B == True) or (A == False and B == False)):
        return True
    else:
        return False
# print(iff(True, True))  
# print(iff(True, False)) 

def xor (A, B):
    if ((A == True and B == True) or (A == False and B == False)):
        return False
    else:
        return True
print(xor(True, True))    
print(xor(True, False))


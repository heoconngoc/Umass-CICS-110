# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

import math 

def cullen(n):
    return n * (2**n) + 1
# print(cullen(1)) 
# print(cullen(5)) 

def woodall (n):
    return n * (2**n) - 1
# print(woodall(1))
# print(woodall(5))

def fermat (n):
    return 2**(2**n)+1
# print(fermat(1)) 
# print(fermat(5)) 

def divides_evenly(dividend, divisor):
    if(dividend % divisor == 0):
        return True
    else:
        return False    
# print(divides_evenly(10, 5))  
# print(divides_evenly(10, 3))

def cone_volume(r, h):
    return math.pi * (r**2) * (h/3)
# print(cone_volume(4, 5))
# print(cone_volume(1, 3)) 


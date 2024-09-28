# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

from logic import nand, implies, iff, xor

def nand_of_tuple (tuple):
    return nand(tuple[0], tuple[1])
# print(nand_of_tuple((True, True)))  
# print(nand_of_tuple((False, True))) 

def implies_in_both_directions (list):
    a = implies(list[0],list[1])
    b = implies(list[1],list[0])
    list[0] = a
    list[1] = b
    return list
# print(implies_in_both_directions([True, True]))  
print(implies_in_both_directions([False, True])) 

def iff_with_result (list):
    list.append(iff(list[0],list[1]))
    return list
# print(iff_with_result([True, True]))
# print(iff_with_result([True, False])) 

def xor_with_result_in_between (list):
    a = xor(list[0],list[1])
    list.insert(1,a)
    return list
# print(xor_with_result_in_between([True, True]))
# print(xor_with_result_in_between([True, False])) 
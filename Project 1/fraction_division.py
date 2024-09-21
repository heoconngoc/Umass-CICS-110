# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

a = int(input("What is the dividend: "))
b = int(input("What is the divisor: "))
quotient = a//b
remainder = (a%b)/b
print(f"{a}/{b} equals:")
print(f"\t{quotient} and {a-b*quotient}/{b}")
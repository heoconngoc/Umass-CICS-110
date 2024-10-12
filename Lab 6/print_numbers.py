# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

n = int(input("Enter a positive integer:"))
for a in range (1,n+1)[::-1]:
    for b in range (1, a):
        print (b, end =' ')
    print(a)

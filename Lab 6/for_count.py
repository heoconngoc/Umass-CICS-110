# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def count_strings(liststr, n: int):
    count = 0
    for str in liststr:
        if(len(str)>=n):
            count += 1      
    return count

def get_factors(n):
    factors = []
    for i in range(2,(n//2)+1):
        if (n%i==0):
            factors.append(i)
    return factors

# print(get_factors(10))            # should return [2, 5]
# print(get_factors(12))            # should return [2, 3, 4, 6]
# print(get_factors(16))            # should return [2, 4, 8]
# print(get_factors(17))            # should return an empty list []



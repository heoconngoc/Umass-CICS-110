# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

def discriminant(a, b, c):
    return b**2 - 4*a*c

# print(discriminant(6, 10, -1)) 
# print(discriminant(1, -3, 4))

def has_real_root(a, b, c):
    d = discriminant(a, b, c)
    if(d>=0):
        return True
    else:
        return False

# print(has_real_root(6, 10, -1))
# print(has_real_root(1, -3, 4))

def get_real_roots(a,b,c):
    d = discriminant(a, b, c)
    x1 = ((-b) + d**(1/2)) / (2*a)
    x2 = ((-b) - d**(1/2)) / (2*a)
    return (x1, x2)

# print(get_real_roots(1, -7, 10))  
# print(get_real_roots(1, -3, -28)) 
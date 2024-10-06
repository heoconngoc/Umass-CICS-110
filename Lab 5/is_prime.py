# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

# def is_prime(n: int):
#     if (n==2):
#         return True
#     a = 2
#     i = (n)**(1/2)
#     while a < (i+1):
#         if n%a != 0:
#             a = a + 1
#         else:
#             return False
#     return True

def is_prime(n: int):
    a = 2
    i = (n)**(1/2)
    print("i là", i)
    while a < (i):
        print("a nhỏ hơn i")
        if n%a != 0:
            print(n%a)
            a = a + 1
            print("a là",a)
        else:
            print(n%a)
            return False
    return True


print(is_prime(64))


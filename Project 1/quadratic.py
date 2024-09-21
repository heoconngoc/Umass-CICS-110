# Author   : Quoc Dat Pham
# Email    : quocdatpham@umass.edu
# Spire ID : 34740949

a = int(input("Enter a:"))
b = int(input("Enter b:"))
c = int(input("Enter c:"))
delta_sr = ((b**2) - (4*a*c))**(1/2)
x1 = (-b + delta_sr) / (2*a)
x2 = (-b - delta_sr) / (2*a)
print(delta_sr)
print(a,"* x^2 +",b,"x +",c,"has roots:")
print(x1)
print(x2)

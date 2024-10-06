a = int(input("Enter a number: "))
sum = 0
i = 1
while i <= a:
    sum += 1/(i**2)
    i += 1
print("sum = ",sum)
print("approximate value of pi is:", (6*sum)**(1/2))
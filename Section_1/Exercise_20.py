from math import sqrt


a0 = int(input("Enter a0: "))
b0 = int(input("Enter b0: "))
epsilon = 0.00001

while a0-b0 > epsilon:
    a1 = (a0+b0)/2
    b1 = sqrt(a0*b0)
    a0 = (a1+b1)/2
    b0 = sqrt(a1*b1)
print(a0)

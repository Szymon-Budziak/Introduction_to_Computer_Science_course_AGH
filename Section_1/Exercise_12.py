"""
Napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb.
"""


def GCD(number1, number2):
    while number2 != 0:
        c = number1 % number2
        number1 = number2
        number2 = c
    return number1


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))

print(GCD(GCD(number1, number2), number3))

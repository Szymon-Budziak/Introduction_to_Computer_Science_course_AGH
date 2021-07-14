"""
Napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb.
"""


def GCD(a, b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a


def LCM(a, b):
    LCM_result = (a * b) / GCD(a, b)
    return LCM_result


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter third number: "))
LCM_result = LCM(LCM(number1, number2), number3)
print(LCM_result)

"""
Napisać program wypisujący wszystkie możliwe podziały liczby naturalnej na sumę składników.
Na przykład dla liczby 4 są to: 1+3, 1+1+2, 1+1+1+1, 2+2.
"""


# MY SOLUTION


def number_division(number, x, y):
    if x == 1:
        print(x, end=" ")
        for j in range(number - 1):
            print("+", x, end=" ")
        print("\t")
        return
    if y == 1:
        print(x, end=" ")
        for i in range(number - x):
            print("+", y, end=" ")
        print("\t")
        number_division(number, x - 1, number - (x - 1))
    elif y != 1:
        print(x, "+", y, end=" ")
        for k in range(number - x - y):
            print("+", number - x - y, end=" ")
        print("\t")
        number_division(number, x, y - 1)


N = 4
number_division(N, N - 1, 1)
print("--------")


# EXERCISE SOLUTION


def number_division2(number, ret=[]):
    if number == 0:
        print(ret)
    for i in range(1, number + 1):
        number_division2(number - i, ret + [i])


number = 4
number_division2(number)

"""
Liczby zespolone są reprezentowane przez krotkę (re, im). Gdzie: re - część rzeczywista liczby,
im - część urojona liczby. Proszę napisać podstawowe operacje na liczbach zespolonych,
m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
"""
from math import sqrt, cos, sin


def addition(a, b):
    return (a[0] + b[0], a[1] + b[1])


def subtraction(a, b):
    return (a[0] - b[0], a[1] - b[1])


def multiplication(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def division(a, b):
    return ((a[0] * b[0] + a[1] * b[1]) / (b[0] ** 2 + b[1] ** 2),
            (a[1] * b[0] - a[0] * b[1]) / (b[0] ** 2 + b[1] ** 2))


def power(a, n):
    z = sqrt(a[0] ** 2 + a[1] ** 2)
    cosx = a[0] / z
    angel = sin(cosx)
    return ((z ** n) * cos(n * angel), (z ** n) * sin(n * angel))


# enter complex number by typing x+yj e.g. 4+6j
def complex_number_input():
    re, im = tuple(map(int, input().split("+i")))
    return re, im


print(complex_number_input())

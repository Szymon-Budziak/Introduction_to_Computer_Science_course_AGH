"""
Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na iloczyn 2 liczb
o najmniejszej różnicy. Np. 30 = 5 ∗ 6, 120 = 10 ∗ 12.
"""
from math import sqrt

number = int(input("Enter a number: "))

for i in range(1, 100):
    if number % i != 0:
        i = sqrt(number)
    i += 1
print(number, "=", round(i), "*", round(number / i))

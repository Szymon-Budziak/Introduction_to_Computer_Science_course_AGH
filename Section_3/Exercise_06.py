"""
Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający
czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
"""
from random import randint

t = list()
N = 1000
for _ in range(N):
    x = randint(1, 1001)
    if x not in t:
        t.append(x)
    else:
        N -= 1
for i in t:
    if (i % 10) % 2 == 1:
        print("Yes", i)
        break

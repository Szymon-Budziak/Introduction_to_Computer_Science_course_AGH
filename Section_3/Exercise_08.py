"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""
from random import randint


def crossing_check(N):
    t = [randint(1, 30) for _ in range(N)]
    print(t)
    for i in range(len(t) - 1):
        aliquot = 2
        copy = t[i]
        count = i
        while copy > 1:
            if copy % aliquot == 0:
                if copy == t[-1]:
                    return True, t[i]
                elif copy != t[-1]:
                    try:
                        copy = t[count + aliquot]
                        count += aliquot
                        aliquot = 2
                    except IndexError:
                        break
            elif copy % aliquot != 0:
                aliquot += 1
                continue
    return False


print(crossing_check(30))

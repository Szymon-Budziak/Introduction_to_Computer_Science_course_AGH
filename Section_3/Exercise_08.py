"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k].
Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
"""
from random import randint


def crossing_check(N):
    T = [randint(1, 30) for _ in range(N)]
    print(T)
    visited = [False] * len(T)
    visited[0] = True
    for i in range(len(T)):
        if visited[i]:
            divisor = 2
            while T[i] > 1:
                while T[i] % divisor == 0:
                    if i + divisor < len(T):
                        visited[i + divisor] = True
                    T[i] //= divisor
                divisor += 1
    return visited[-1]


print(crossing_check(30))

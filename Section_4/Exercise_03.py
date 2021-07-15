"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada
na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę parzystą.
"""
from random import randint


def has_even(array):
    count = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] % 2 == 0:
                count += 1
            elif array[i][j] % 2 != 0:
                while array[i][j] > 0:
                    r = array[i][j] % 10
                    array[i][j] //= 10
                    if r % 2 == 0:
                        count += 1
                        break
        if count == N:
            return True
    return False


N = 5
array = [[randint(0, 100) for _ in range(N)] for _ in range(N)]
print(has_even(array))

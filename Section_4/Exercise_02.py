"""
Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która odpowiada
na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
z nieparzystych cyfr.
"""
from random import randint


def is_only_odd(array):
    for i in range(len(array)):
        count = 0
        for j in range(N):
            if array[i][j] % 2 == 0:
                continue
            elif array[i][j] % 2 != 0:
                while array[i][j] > 0:
                    r = array[i][j] % 10
                    array[i][j] //= 10
                    if r % 2 != 0 and array[i][j] == 0:
                        count += 1
        if count == 0:
            return False
    return True


N = 5
array = [[randint(0, 100) for _ in range(N)] for _ in range(N)]
print(is_only_odd(array))

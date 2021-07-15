"""
Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie M=N*N.
W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby naturalne.
Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
T2 były uporządkowane niemalejąco.
"""
from random import randint


def non_decreasing_elements(array1, array2, M, N):
    for j in range(N):
        for k in range(N):
            array2 += [array1[j][k]]
            array2 = array2[1:]
    array2.sort()
    return array2


N = 4
M = N ** 2
array1 = [[randint(1, 10) for _ in range(N)] for _ in range(N)]
array2 = [0 for i in range(M)]
print(non_decreasing_elements(array1, array2, M, N))

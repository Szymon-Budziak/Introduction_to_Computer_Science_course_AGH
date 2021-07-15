"""
Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami
naturalnymi po spirali.
"""


# 1ST SOLUTION


def spiral(array):
    n = 1
    low = 0
    high = len(array) - 1
    count = int((len(array) + 1) / 2)
    for i in range(count):
        for j in range(low, high + 1):
            array[i][j] = n
            n += 1
        for j in range(low + 1, high + 1):
            array[j][high] = n
            n += 1
        for j in range(high - 1, low - 1, -1):
            array[high][j] = n
            n += 1
        for j in range(high - 1, low, -1):
            array[j][low] = n
            n += 1
        low += 1
        high -= 1

    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end="\t")
        print()


# 2ND SOLUTION


def spiral_of_natural_numbers(array):
    n = len(array)
    k = 1
    a = 0
    b = n - 1
    while a <= b:
        for i in range(a, b + 1):
            array[a][i] = k
            k += 1
        for i in range(a + 1, b):
            array[i][b] = k
            k += 1
        for i in range(b, a, -1):
            array[b - 1][i] = k
            k += 1
        for i in range(b, a, -1):
            array[i][a] = k
            k += 1
        a += 1
        b -= 1
    return array


array = [[0 for _ in range(4)] for _ in range(4)]
print(spiral_of_natural_numbers(array))

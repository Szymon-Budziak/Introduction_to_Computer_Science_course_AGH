from random import randint


def nondecreasing_elements(array1, array2, M, N):
    for j in range(N):
        for k in range(N):
            array2 += [array1[j][k]]
            array2 = array2[1:]
    array2.sort()
    return array2


N = 4
M = N**2
array1 = [[randint(1, 10) for _ in range(N)] for _ in range(N)]
array2 = [0 for i in range(M)]
print(nondecreasing_elements(array1, array2, M, N))

from random import randint


def all_singletons(array1, array2, N):
    for i in range(N):
        array1[i].sort()
    for j in range(N):
        for k in range(N):
            if array1[j][k] not in array2:
                array2 += [array1[j][k]]
    array2.sort()
    m = 0
    while array2[m] == 0:
        array2.remove(array2[m])
    return array2


N = 5
M = N**2
array1 = [[randint(1, 100) for _ in range(N)] for _ in range(N)]
array2 = [0 for k in range(M)]
print(all_singletons(array1, array2, N))

from random import randint


def is_there_at_least_one_0(array):
    result = 0
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i][j] == 0:
                result += 1
                break
    for a in range(len(array)):
        for b in range(len(array)):
            if array[b][a] == 0:
                result += 1
                break
    if result == 2*len(array):
        return True
    return False


N = 4
array = [[randint(-3, 3) for _ in range(N)] for _ in range(N)]
print(is_there_at_least_one_0(array))

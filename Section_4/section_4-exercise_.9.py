from random import randint


def find_square(array, k):
    array_len = len(array)
    array_len_2 = array_len//2
    for i in range(array_len//2):
        if array_len % 2 == 1 and array_len > 1:
            for j in range(array_len//2):
                if (array[0+j][0+j] * array[0+j][-1-j] * array[-1-j][0+j]
                        * array[-1-j][-1-j]) == k:
                    return True, array[array_len_2][array_len_2]
    return False


N = 5
k = 0
array = [[randint(0, 10) for _ in range(N)] for _ in range(N)]
print(find_square(array, k))

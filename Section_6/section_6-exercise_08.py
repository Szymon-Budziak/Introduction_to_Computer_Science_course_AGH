from random import randint


def is_both_mass(array, n, p=0, result=[]):
    if n == 0:
        return True
    elif p == len(array):
        return False
    return (is_both_mass(array, n - array[p], p+1, result + [array[p]])
            or is_both_mass(array, n, p+1, result)
            or is_both_mass(array, n + array[p], p+1, result+[-array[p]]))


N = 4
number = 20
array = [randint(1, 10) for _ in range(N)]
print(is_both_mass(array, number))

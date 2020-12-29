from random import randint


def only_one_max_min_element(t, x):
    len_t = len(t)
    result1 = 0
    result2 = 0
    minimum_value = x+1
    maximum_value = -x-1
    for i in range(len_t):
        if t[i] <= minimum_value:
            if t[i] == minimum_value:
                result1 += 1
            elif t[i] != minimum_value:
                result1 = 0
            minimum_value = t[i]
    for k in range(len_t):
        if t[k] >= maximum_value:
            if t[i] == maximum_value:
                result2 += 1
            elif t[i] != maximum_value:
                result2 = 0
            maximum_value = t[k]
    if result1 > 0 or result2 > 0:
        return False
    else:
        return True


n = int(input("Enter range of array: "))
x = int(input("Enter max array value: "))
t = [randint(-abs(x), abs(x)) for _ in range(n)]
print(t)
print(only_one_max_min_element(t, x))

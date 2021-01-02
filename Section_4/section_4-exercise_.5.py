from random import randint


def integers_sum_quotient(array):
    count = 0
    maximum = 0
    column = 0
    row = 0
    for j in range(len(array)):
        for i in range(len(array)):
            count += array[i][j]
        for x in range(N):
            if array[x][j] == 0:
                continue
            else:
                maxNumber = count/array[x][j]
                if maxNumber > maximum:
                    maximum = maxNumber
                    column = x
                    row = j
        count = 0
    return column, row


N = 4
array = [[randint(-100, 100) for _ in range(N)] for _ in range(N)]
print(integers_sum_quotient(array))

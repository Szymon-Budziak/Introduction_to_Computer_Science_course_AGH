from random import randint


def sum_quotient(array):
    count = 0
    maximum = 0
    column = 0
    row = 0
    for j in range(len(array)):
        for i in range(len(array)):
            count += array[i][j]
        for x in range(N):
            maxNumber = count/array[x][j]
            if maxNumber > maximum:
                maximum = maxNumber
                column = x
                row = j
        count = 0
    return column, row


N = 4
array = [[randint(1, 10000) for _ in range(N)] for _ in range(N)]
print(sum_quotient(array))

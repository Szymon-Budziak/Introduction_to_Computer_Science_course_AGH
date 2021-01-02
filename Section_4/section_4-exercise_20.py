from random import randint


def column_summary(array, row, col):
    result = 0
    for i in range(len(array)):
        result += array[i][col]
    result -= array[row][col]
    return result


def row_summary(array, row, col):
    result = 0
    for i in range(len(array)):
        result += array[row][i]
    result -= array[row][col]
    return result


def two_rooks(array):
    result = 0
    max_result = 0
    for i in range(len(array)):
        for j in range(len(array)):
            for k in range(i, len(array)):
                for m in range(j, len(array)):
                    if i != k and j != m:
                        result = column_summary(array, i, j) \
                            + column_summary(array, k, m) \
                            + row_summary(array, i, j) \
                            + row_summary(array, k, m)
                        result -= array[i][m]
                        result -= array[k][j]
                        if result > max_result:
                            tower_1 = (i, j)
                            tower_2 = (k, m)
                            max_result = result
    return (tower_1[0], tower_1[1], tower_2[0], tower_2[1])


N = 5
array = [[randint(1, 10) for _ in range(N)] for _ in range(N)]
print(two_rooks(array))

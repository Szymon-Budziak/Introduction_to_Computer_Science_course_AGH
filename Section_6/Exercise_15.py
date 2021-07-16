"""
Problem 8 Hetmanów (treść oczywista).
"""


def is_move_possible(T, row, column):
    for i in range(len(T)):
        if T[row][i] == 1:
            return False
    for j in range(len(T)):
        if T[j][column] == 1:
            return False
    for k in range(len(T)):
        for m in range(len(T)):
            if T[k][m] == 1:
                if abs(k - row) == abs(m - column):
                    return False
    return True


def chess_queen(T):
    T_len = len(T)
    for i in range(T_len):
        for j in range(T_len):
            if T[i][j] == 0:
                if is_move_possible(T, i, j):
                    T[i][j] = 1
                    chess_queen(T)
                    if sum(sum(a) for a in T) == T_len:
                        return T
                    T[i][j] = 0
    return T


T = [[0 for _ in range(8)] for i in range(8)]
print(chess_queen(T))

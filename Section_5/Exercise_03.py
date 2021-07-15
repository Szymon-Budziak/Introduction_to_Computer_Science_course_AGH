"""
Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie hetmanów jest
opisywane przez tablicę dane = [(w[1], k[1]), (w[2], k[2]), (w[3], k[3]), ..., (w[N], k[N])].
Proszę napisać funkcję, która odpowiada na pytanie: czy żadne z dwa hetmany się nie szachują?
Do funkcji należy przekazać położenie hetmanów.
"""
from random import randint


def queen_check(queen, N):
    for i in range(N):
        for j in range(i + 1, N):
            if queen[i][0] == queen[j][0] or queen[i][1] == queen[j][1]:
                return False
            elif abs(queen[i][0] - queen[j][0]) == abs(queen[i][1] - queen[j][1]):
                return False
    return True


N = 4
queen = [(randint(0, 9), randint(0, 9)) for _ in range(N)]
chessboard = [[(" ", " ") for _ in range(10)] for _ in range(8)]
print(queen_check(queen, N))

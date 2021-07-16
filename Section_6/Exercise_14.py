"""
Problem wież w Hanoi (treść oczywista).
"""


def hanoi_tower(n, result):
    result[0] += 1
    if n == 1:
        return
    hanoi_tower(n - 1, result)
    hanoi_tower(n - 1, result)
    return result[0]


result = [0]
print(hanoi_tower(3, result))

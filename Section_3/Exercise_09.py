"""
Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
długość najdłuższego, spójnego podciągu rosnącego.
"""
from random import randint


def longest_increasing_subsequence(T):
    if len(T) <= 1:
        return len(T)
    max_length = actual_length = 1
    for i in range(1, len(T)):
        if T[i - 1] < T[i]:
            actual_length += 1
        else:
            max_length = max(max_length, actual_length)
            actual_length = 1
    return max_length


n = int(input("Enter a range: "))
T = [randint(0, 100) for _ in range(n)]
print(longest_increasing_subsequence(T))

"""
Proszę napisać program, który wypełnia N-elementową tablicę t pseudolosowymi liczbami
nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością
najdłuższego znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy, a długością
najdłuższego ciągu arytmetycznego o ujemnej różnicy, przy założeniu, że kolejnymi wyrazami
ciągu są elementy tablicy o kolejnych indeksach.
"""
from random import randint


def the_longest_sequence():
    t = list()
    N = 100
    i = 1
    j = 1
    last_difference = longest_increasing = longest_decreasing = current_sequence_length = 1
    for i in range(N):
        x = randint(1, N)
        if x not in t and x % 2 == 1:
            t.append(x)
        else:
            i -= 1
    print(t)
    result = 1
    while j < len(t):
        current_difference = t[j] - t[j - 1]
        if current_difference == last_difference:
            current_sequence_length += 1
        else:
            current_sequence_length = 2
            last_difference = current_difference
        if last_difference > 0:
            longest_increasing = max(longest_increasing, current_sequence_length)
        elif last_difference < 0:
            longest_decreasing = max(longest_decreasing, current_sequence_length)
        j += 1
        result = longest_increasing - longest_decreasing
    return result


print(the_longest_sequence())

"""
Napisać program wyszukujący liczby doskonałe mniejsze od miliona.
"""
number = 1000000
for i in range(1, number + 1):
    summary = 0
    for j in range(1, (i // 2) + 1):
        if i % j == 0:
            summary += j
    if summary == i:
        print(summary)

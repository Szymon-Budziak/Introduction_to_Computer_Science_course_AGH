from math import inf

min_sum = inf
best_result = (2020, 0)
for i in range(2021):
    a, b = 2020, i
    while a > b > 0:
        a, b = b, a - b
    if a + b < min_sum:
        min_sum = a + b
        best_result = (b, a)
print(min_sum, best_result)

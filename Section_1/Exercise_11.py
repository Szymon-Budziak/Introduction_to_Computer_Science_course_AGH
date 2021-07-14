"""
Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.
"""
number = 1
result1 = 0
result2 = 0
while number < 1000000:
    for i in range(1, number):
        if number % i == 0:
            result1 += i
    result1_factor = result1

    for j in range(1, result1_factor):
        if result1_factor % j == 0:
            result2 += j
    result2_factor = result2

    if number == result2_factor:
        if number != result1_factor:
            print("Numbers", number, "and", result1_factor,
                  "are amicable numbers.")
    result1 = 0
    result2 = 0
    number += 1

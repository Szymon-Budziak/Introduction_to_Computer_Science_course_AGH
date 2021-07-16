"""
Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie muszą
wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375, 17523,
75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
zadanych liczb.
"""
from math import sqrt


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def length(number):
    count = 0
    while number > 0:
        number //= 10
        count += 1
    return count


def create_number(number_1, number_2, idx):
    length_1 = length(number_1)
    length_2 = length(number_2)
    new_number = (number_2 // (10 ** (length_2 - idx))) * 10 ** length_1 + number_1
    new_number *= 10 ** (length_2 - idx)
    new_number += number_2 % (10 ** (length_2 - idx))
    return new_number


def number_of_created_numbers(number_1, number_2):
    count = 0
    for i in range(length(number_1)):
        actual_number = create_number(number_2, number_1, i)
        if prime_number(actual_number):
            count += 1
    for i in range(length(number_2)):
        actual_number = create_number(number_1, number_2, i)
        if prime_number(actual_number):
            count += 1
    return count


print(number_of_created_numbers(19, 61))

"""
Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000. Proszę napisać
funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy, dla którego w iloczynie
jego elementów każdy czynniki pierwszy występuje co najwyżej raz. Na przykład dla tablicy
t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.
"""
from math import sqrt, ceil


def prime_factor_occurs_once(number):
    if number % 4 == 0:
        return False
    for i in range(3, ceil(sqrt(number)) + 1):
        if number % i == 0:
            number //= i
        if number % i == 0:
            return False
    return True


def longest_sequence(T):
    max_length = 0
    for i in range(len(T)):
        actual_length = 0
        j = i + 1
        product = T[i]
        while j < len(T) and prime_factor_occurs_once(product):
            product *= T[j]
            j += 1
            actual_length += 1
        max_length = max(max_length, actual_length)
    return max_length


T = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(longest_sequence(T))

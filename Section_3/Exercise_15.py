"""
Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy zachodzi
następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”.
"""
from random import randint


def fibonacci_index(t):
    len_t = len(t)
    a = 0
    b = 1
    for i in range(0, len_t):
        result_a = 0
        result_b = 0
        try:
            a_str = str(t[a])
            b_str = str(t[b])
            for x in range(len(a_str)):
                result_a += 1
            for y in range(len(b_str)):
                result_b += 1
            if result_a > 1 and result_b > 1:
                a += b
                b += a
                continue
            else:
                return False
        except IndexError:
            continue
    return True


t = [randint(1, 100) for _ in range(10)]
print(fibonacci_index(t))

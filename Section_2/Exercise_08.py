"""
Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu Fibonacciego,
np. 9, 14, 15, 17, 22. Proszę napisać program, który wczytuje liczbę naturalną n, wylicza i wypisuje
następną taką liczbę większą od n. Można założyć, że 0 < n < 1000.
"""


def is_fib_sum(number):
    a = 1
    b = 1

    while a < number and b < number:
        a = a + b
        b = a + b
        if a == number or b == number:
            return "Number is in Fibonacci sequence."
        else:
            continue
    if a > number:
        return a
    elif b > number:
        return b


number = int(input("Enter a number: "))
print(is_fib_sum(number))

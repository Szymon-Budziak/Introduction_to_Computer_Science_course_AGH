"""
”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory
o równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość
typu Bool.
"""


def weight(n):
    count = 0
    k = 2
    while n > 1 and k <= n:
        if n % k == 0:
            count += 1
            while n % k == 0:
                n //= k
        k += 1
    return count


def can_be_summered(T, sum1=0, sum2=0, sum3=0, i=0):
    if sum1 > 0 and sum1 == sum2 and sum2 == sum3:
        return True
    elif i == len(T):
        return False
    return (can_be_summered(T, sum1 + T[i], sum2, sum3, i + 1) or
            can_be_summered(T, sum1, sum2 + T[i], sum3, i + 1) or
            can_be_summered(T, sum1, sum2, sum3 + T[i], i + 1))


def subsets_of_equal_weights(T):
    summary = 0
    for i in range(len(T)):
        T[i] = weight(T[i])
        summary += T[i]
    if summary % 3 == 0:
        if can_be_summered(T):
            return True
    else:
        return False


T = [9, 16, 12, 17, 8]
print(subsets_of_equal_weights(T))

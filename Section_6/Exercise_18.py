"""
W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla nałożono
dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby
na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
obranego celu (np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu.
Dana jest globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę.
Lewy górny narożnik ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może
dostać się z pola w,k do prawego dolnego narożnika.
"""
from random import randint


def distance(T, x, y):
    distance = abs(len(T) - 1 - x) + abs(len(T) - 1 - y)
    return distance


def chess_king(T, w, k, actual_distance):
    if w == (len(T) - 1) and k == (len(T) - 1):
        return True
    temporary = False
    if w <= len(T) - 1 and k <= len(T) - 1 and w >= 0 and k >= 0:
        if distance(T, w + 1, k) < actual_distance and T[w][k] % 10 < T[w + 1][k]:
            current_distance1 = distance(T, w + 1, k)
            chess_king(T, w + 1, k, current_distance1)
        if distance(T, w, k + 1) < actual_distance and T[w][k] % 10 < T[w][k + 1]:
            current_distance2 = distance(T, w, k + 1)
            chess_king(T, w, k + 1, current_distance2)
        if distance(T, w + 1, k + 1) < actual_distance and T[w][k] % 10 < T[w + 1][k + 1]:
            current_distance3 = distance(T, w + 1, k + 1)
            temporary = temporary or chess_king(T, w + 1, k + 1, current_distance3)
    return temporary


w, k = 0, 0
T = [[randint(1, 50) for _ in range(8)] for i in range(8)]
actual_distance = abs(len(T) - 1 - w) + abs(len(T) - 1 - k)
print(chess_king(T, 0, 0, actual_distance))

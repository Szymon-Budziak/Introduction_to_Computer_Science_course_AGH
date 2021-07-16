"""
Szachownica jest reprezentowana przez tablicę T[8][8] wypełnioną liczbami naturalnymi zawierającymi
koszt przebywania na danym polu szachownicy. Król szachowy znajduje się w wierszu 0 i kolumnie k.
Król musi w dokładnie 7 ruchach dotrzeć do wiersza 7. Proszę napisać funkcję, która wyznaczy minimalny
koszt przejścia króla. Do funkcji należy przekazać tablicę t oraz startową kolumnę k. Koszt
przebywania na polu startowym i ostatnim także wliczamy do kosztu przejścia.
"""
from random import randint


def chess_king(i, k, field_cost_result):
    field_cost_result += array[i][k]
    summary = -1
    if i == 7:
        return field_cost_result
    else:
        for x in range(k - 1, k + 2):
            if x >= 0 and x < 8:
                if summary == -1:
                    summary = chess_king(i + 1, x, field_cost_result)
                else:
                    summary = min(chess_king(
                        i + 1, x, field_cost_result), summary)
    return summary


k = randint(0, 7)
array = [[randint(1, 9) for _ in range(8)] for _ in range(8)]
print(chess_king(0, k, 0))

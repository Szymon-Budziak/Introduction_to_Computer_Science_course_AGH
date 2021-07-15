"""
Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w grupie N przypadkowo
spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć wartości
prawdopodobieństwa dla N z zakresu 20-40.
"""


def probability(index):
    count = 1
    for i in range(index):
        count *= (1 - i / 365)
    return 1 - count


def probability_of_being_born_same_day():
    start = 20
    while start <= 40:
        print(start, probability(start))
        start += 1


probability_of_being_born_same_day()

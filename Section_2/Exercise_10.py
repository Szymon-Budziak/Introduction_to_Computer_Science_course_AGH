"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A[n] = 3 ∗ A[n−1] + 1,
a pierwszy wyraz jest równy 2.
"""
number = int(input("Enter a number: "))
an = 2

while True:
    an = (3 * an) + 1
    if an / number == int(an / number):
        print("Number", number, "is a multiple of a number", an)
        break
    else:
        print("Number", number, "isn't a multiple of a number", an)

"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy jej cyfry stanowią ciąg rosnący.
"""


def are_digits_incresing(strnumber, i):
    while i != len(strnumber):
        if strnumber[i] > strnumber[i - 1]:
            i += 1
        elif len(strnumber) < len(strnumber) - 2:
            return False
        elif strnumber[i] < strnumber[i - 1]:
            return False
    return True


number = int(input("Enter a number: "))
str_number = str(number)
print(are_digits_incresing(str_number, i=1))

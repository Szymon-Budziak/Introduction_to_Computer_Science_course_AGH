"""
Napisać program, który oblicza pole figury pod wykresem funkcji y = 1/x w przedziale
od 1 do k, metodą prostokątów.
"""
number = int(input("Enter a number: "))
k = int(input("Enter a range: "))
n = int(input("How many rectangles do you want to split the diagram into: "))
a = (k - 1) / n
summary = 0
center = 1 + (k - 1) / 2 * n
i = 0


def figure_area(a):
    return a * a + a + 2


if number == 0:
    print("You have to enter number different from 0.")
else:
    while i < k:
        summary += figure_area(center)
        center += a
        i += 1
    print(summary * a)

"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.
"""
a = int(input("Enter a number: "))
b = 0
d = a

while a > 0:
    c = a % 10
    a = a // 10
    b = b * 10 + c
if b == d:
    print("Yes ")
else:
    print("No")

"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.
"""
number = int(input("Enter a number: "))
starting_number = 1
a = 1
b = 1
flag = True
while starting_number < 1000:
    while a < 1000:
        a = a + b
        if (a * b) == number:
            print("Number", number, "is product of", a, "and",
                  b, "which belong to the Fibonacci sequence.")
            flag = False
            break
        b = a + b
        if (a * b) == number:
            print("Number", number, "is product of", a, "and",
                  b, "which belong to the Fibonacci sequence.")
            flag = False
            break
    starting_number += 1

if flag:
    print("Number is not a product of any two numbers which belong to the Fibonacci sequence.")

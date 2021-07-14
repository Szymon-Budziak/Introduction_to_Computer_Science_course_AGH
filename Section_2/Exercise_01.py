"""
Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
"""


def is_product_of_Fib(number, a, b):
    while number > a * b:
        a = a + b
        b = a + b
    if number == a * b:
        return True
    return False


number = int(input("Enter a number: "))
print(is_product_of_Fib(number, a=1, b=1))

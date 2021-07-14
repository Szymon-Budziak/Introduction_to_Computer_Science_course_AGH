"""
Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.
"""
number = int(input("Enter sum to check: "))
a1 = 0
b1 = 1
a2 = 0
b2 = 1
amount = 0
while b1 <= b2 and amount >= 0:
    if amount == number:
        print("Exist")
        break
    elif amount < number:
        amount += b2
        b2 += a2
        a2 = b2 - a2
    elif amount > number:
        amount -= b1
        b1 += a1
        a1 = b1 - a1
        if amount < number:
            print("Doesn't exist")
            break

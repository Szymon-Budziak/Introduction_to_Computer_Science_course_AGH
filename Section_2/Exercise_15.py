"""
Napisać program znajdujący wszystkie liczby N-cyfrowe dla których suma N-tych potęg cyfr
liczby jest równa tej liczbie, np. 153 = 1**3 + 5**3 + 3**3 .
"""


def mathematical_power(number):
    while number > 0:
        a = number
        power = 1
        number_check = 0
        i = 0
        strnumber = str(number)
        while strnumber[i:-1:1]:
            power += 1
            i += 1
        x = power
        while a > 0:
            c = a % 10
            a = a // 10
            number_check += c ** x
        if number_check == number:
            print(number)
        number -= 1


number = 100000
mathematical_power(number)

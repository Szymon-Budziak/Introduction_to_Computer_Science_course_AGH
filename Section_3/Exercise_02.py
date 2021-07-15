"""
Napisać program wczytujący dwie liczby naturalne i odpowiadający na pytanie czy są one
zbudowane z takich samych cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.
"""


def number_check(number1, number2):
    number_list = list()
    number1_string = str(number1)
    number2_string = str(number2)
    number1_counter = 0
    number2_counter = 0
    i = 0
    j = 0
    while number1 > 0:
        number1 //= 10
        number1_counter += 1
    while number2 > 0:
        number2 //= 10
        number2_counter += 1
    for i in range(number1_counter):
        number_list.append(number1_string[i])
    for j in range(number2_counter):
        if number2_string[j] not in number_list:
            return False
        else:
            continue
    return True


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
print(number_check(number1, number2))

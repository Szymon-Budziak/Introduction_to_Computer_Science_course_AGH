def number_base_converter(number, base):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return a


def different_digits(number_1, number_2):
    while True:
        for i in range(3, 17):
            count = 0
            change_1 = number_base_converter(number_1, i)
            change_2 = number_base_converter(number_2, i)
            for j in range(len(change_1)):
                if change_1[j] not in change_2:
                    count += 1
                if count == len(change_1):
                    return i
        return False


print(different_digits(123, 522))

from math import log
from math import ceil


# 1ST SOLUTION


def number_base_converter(number, base):
    hex = "0123456789ABCDEF"
    resultList = [0 for _ in range(ceil(log(number, base)))]
    i = 0
    while number > 0:
        resultList[i] = number % base
        number //= base
        i += 1
    resultList.reverse()
    for j in resultList:
        print(hex[j], end="")


# 2ND SOLUTION


def base_convert(number, base):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % base] + a
        number = number // base
    return a


# 3RD RECURSION SOLUTION


def recursion_base_converter(number, base):
    if number == 0:
        return
    result = number % base
    recursion_base_converter(number//base, base)
    if result > 9:
        result = chr(ord('A') + result-10)
    print(result)

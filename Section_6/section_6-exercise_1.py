from math import sqrt
from math import log10


# 1ST SOLUTION


def prime_number(a):
    if a == 2 or a == 3:
        return True
    elif a < 2 or a % 2 == 0 or a % 3 == 0:
        return False
    else:
        i = 5
        while i <= sqrt(a):
            if a % i == 0:
                return False
            i += 2
            if a % i == 0:
                return False
            i += 4
        return True


def double_digit_prime_number(number):
    number_of_digits = int((log10(number) + 1)//1)
    for i in range(0, number_of_digits):
        for j in range(i+1, number_of_digits):
            strnumber = str(number)
            copy_number = strnumber[i:j] + strnumber[j+1:]
            int_copy_number = int(copy_number)
            double_digit_prime_number(int_copy_number)
            if int_copy_number // 10 > 0 and prime_number(int_copy_number):
                print(int_copy_number)


number = 14357
double_digit_prime_number(number)


# 2ND SOLUTION


def double_digit_prime_number2(number, x=0, p=0, b=False):
    if number == 0:
        if x > 9 and b and prime_number(x):
            print(x)
    else:
        double_digit_prime_number2(number//10, (10**p)*(number % 10)+x, p+1, b)
        double_digit_prime_number2(number//10, x, p, True)

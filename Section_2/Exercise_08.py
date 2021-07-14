def isFibSum(number):
    a = 1
    b = 1

    while a < number and b < number:
        a = a+b
        b = a+b
        if a == number or b == number:
            return "Number is in Fibonacci sequence."
        else:
            continue

    if a > number:
        return a
    elif b > number:
        return b


number = int(input("Enter a number: "))
print(isFibSum(number))

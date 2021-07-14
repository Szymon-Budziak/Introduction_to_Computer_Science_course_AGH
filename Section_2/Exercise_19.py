def how_many_2_5(n):
    numerator2 = 0
    while n % 2 == 0:
        numerator2 += 1
        n //= 2

    numerator5 = 0
    while n % 5 == 0:
        numerator5 += 1
        n //= 5

    return max(numerator2, numerator5)


numerator = int(input("Enter numerator: "))
denominator = int(input("Enter denominator: "))
remainder = numerator % denominator
print(numerator//denominator, end="")

if remainder > 0:
    print(".", end="")
    for i in range(how_many_2_5(denominator)):
        remainder *= 10
        print(remainder//denominator, end="")
        remainder %= denominator
    if remainder > 0:
        print("(", end="")
        memory = remainder
        while True:
            remainder *= 10
            print(remainder//denominator, end="")
            remainder %= denominator
            if remainder == memory:
                break
        print(")")

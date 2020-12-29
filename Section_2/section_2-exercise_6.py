from math import sqrt


number = int(input("Enter a number: "))

for i in range(1, 100):
    if number % i != 0:
        i = sqrt(number)
    i += 1
print(number, "=", round(i), "*", round(number/i))

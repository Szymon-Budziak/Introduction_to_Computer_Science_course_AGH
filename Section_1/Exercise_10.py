number = 1000
result = 0
while number > 1:
    for i in range(1, number + 1):
        if number % i == 0:
            result += i
            if result == number:
                print("Number", number, "is perfect number.")
    result = 0
    number -= 1

number = int(input("Enter a number: "))
starting_number = 1
a = 1
b = 1
while starting_number < 1000:
    while a < 1000:
        a = a + b
        if (a * b) == number:
            print("Number", number, "is product of", a, "and",
                  b, "which belong to the Fibonacci sequence.")
            break
        b = a + b
        if (a * b) == number:
            print("Number", number, "is product of", a, "and",
                  b, "which belong to the Fibonacci sequence.")
            break
    starting_number += 1

number = int(input("Enter a number: "))
starting_number = 1
i = 0
result = 1
while result <= number:
    starting_number += 2
    result += starting_number
    i += 1
print("Element of this number is:", i)

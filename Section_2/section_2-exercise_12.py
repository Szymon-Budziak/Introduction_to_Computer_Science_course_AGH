number = int(input("Enter a number: "))
strnumber = str(number)
i = 0
result = 1

while strnumber[i] != strnumber[-1]:
    result += 1
    i += 1
strresult = str(result)
j = -1

while True:
    if strnumber[j] == strresult:
        print("The number contains a digit equal to the number of its digits.")
        break
    else:
        j -= 1

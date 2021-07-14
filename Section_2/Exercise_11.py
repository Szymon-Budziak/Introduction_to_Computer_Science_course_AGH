def are_digits_incresing(strnumber, i):
    while i != len(strnumber):
        if strnumber[i] > strnumber[i-1]:
            i += 1
        elif len(strnumber) < len(strnumber)-2:
            return False
        elif strnumber[i] < strnumber[i-1]:
            return False
    return True


number = int(input("Enter a number: "))
strnumber = str(number)
print(are_digits_incresing(strnumber, i=1))

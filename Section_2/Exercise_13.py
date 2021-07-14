def unique_number_check(number):
    strnumber = str(number)
    lastnumber = number % 10
    for i in range(len(strnumber)-1):
        if strnumber[i] != str(lastnumber):
            continue
        else:
            return False
    return True


number = int(input("Enter a number: "))
print(unique_number_check(number))

number = int(input("Enter a number: "))
an = 2

while True:
    an = (3*an)+1
    if an/number == int(an/number):
        print("Number", number, "is a multiple of a number", an)
        break
    else:
        print("Number", number, "isn't a multiple of a number", an)

number = int(input("Enter a number: "))
n = 1

while True:
    n = n*n+n+1
    if n/number == int(n/number):
        print("Number", number, "is a multiple of the number", n)
        break
    else:
        print("Number", number, "isn't a multiple of the number", n)

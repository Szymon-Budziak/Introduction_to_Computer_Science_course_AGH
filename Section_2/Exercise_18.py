def sequence(number, a0, a1, b0):
    a2 = a1-(b0*a0)
    b1 = b0+2*a0
    while number != a0:
        print(b1)
        a0 = a1
        a1 = a2
        b0 = b1
        a2 = a2 = a1-(b0*a0)
        b1 = b1 = b0+2*a0


number = int(input("Enter a number: "))
sequence(number, a0=0, a1=1, b0=2)

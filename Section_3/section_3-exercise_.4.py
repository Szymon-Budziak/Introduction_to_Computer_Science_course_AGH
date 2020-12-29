n = int(input("Enter n: "))
e = 1
factorial = 1

for j in range(1, n+1):
    factorial *= j
    e += 1/factorial
print(e, " = ", end="", sep="")

for i in range(0, n+1):
    i_string = str(i)
    print("1/" + i_string + "! + ", end="")

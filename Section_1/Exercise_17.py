def Fibonacci(a, b):
    while a < 1000:
        a = a + b
        b = a + b
    quotient = a / b
    return quotient


number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = Fibonacci(number1, number2)
print("The quotient of the two consecutive numbers of the sequence tends to",
      result)

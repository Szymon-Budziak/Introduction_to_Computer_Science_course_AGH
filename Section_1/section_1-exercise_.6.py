epsilon = 0.000001
number = 2020
a = 0
b = 10
while abs(b-a) > epsilon:
    m = (a+b)/2
    if m**m > number:
        b = m
    else:
        a = m
print(m)

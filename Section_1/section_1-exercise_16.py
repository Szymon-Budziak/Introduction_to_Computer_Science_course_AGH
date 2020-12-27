a0 = 2
m = 1

for a0 in range(2, 10000):
    n = 0
    while a0 != 1:
        a0 = (((a0 % 2)*(3*a0+1))+((1-(a0 % 2))*(a0/2)))
        n += 1
    if n > m:
        m = n
    a0 += 1
print(m)

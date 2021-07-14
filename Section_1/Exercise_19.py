n = 1
e = 0

for i in range(1, 30):
    n = n * i
    e = 1 / n + e
    i += 1
print("e =", 1 + e)

from random import randint


t = list()
N = 1000
for _ in range(N):
    x = randint(1, 1001)
    if x not in t:
        t.append(x)
    else:
        N -= 1
for i in t:
    if (i % 10) % 2 == 1:
        print("Yes", i)
        break

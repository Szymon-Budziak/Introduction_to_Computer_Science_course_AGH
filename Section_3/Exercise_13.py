"""
Proszę napisać program, który wypełnia N-elementową tablicę t trzycyfrowymi liczbami pseudolosowymi,
a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy
dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy:
t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.
"""
t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
max_len = 0
len_t = len(t)
for i in range(len_t):
    result = 0
    cpi = i
    try:
        for k in range(t[-1] - 1, -1, -1):
            if t[k] == t[cpi] and t[k - 1] == t[cpi + 1]:
                cpi = cpi + 1
                result += 1
        if result > max_len:
            max_len = result
    except IndexError:
        continue
print(max_len)

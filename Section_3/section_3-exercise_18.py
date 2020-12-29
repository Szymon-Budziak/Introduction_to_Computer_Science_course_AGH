def find_the_longest_palindrom(t):
    len_t = len(t)
    max_len = 0
    for p in range(len_t):
        if t[p] % 2 == 1:
            for k in range(len_t-1, p-1, -1):
                cp = p
                ck = k
                while cp < ck:
                    if t[cp] != t[ck] or t[cp] % 2 == 0:
                        break
                    cp += 1
                    ck -= 1
                if not (cp < ck):
                    max_len = max(max_len, k-p+1)
    return max_len


t = [1, 3, 3, 1, 4, 8]
print(find_the_longest_palindrom(t))

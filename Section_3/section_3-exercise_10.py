def find_the_longest_arithmetic_progression(t):
    max_len = 0
    len_t = len(t)

    for p in range(len_t):
        for k in range(1, len_t-p):
            result = 1
            r = t[p+k] - t[p]
            cp = p
            ck = k
            while True:
                try:
                    if t[cp+ck] != t[cp] + r:
                        break
                    cp = cp + ck
                    result += 1
                except IndexError:
                    break
            if result > max_len:
                max_len = result
    return max_len


array = [1, 2, 3, 4, 5, 6, 7, 456, 2, 54, 48, 10, 11]
print(find_the_longest_arithmetic_progression(array))

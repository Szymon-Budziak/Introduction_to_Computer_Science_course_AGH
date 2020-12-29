from random import randint


def find_the_longest_conseq_subseq():
    t = list()
    N = 1000
    i = 0
    summary = 0
    count = 0
    ans = 0
    for _ in range(1, N):
        x = randint(1, N)
        if x not in t:
            t.append(x)
        else:
            N -= 1
    t.sort()
    for element in t:
        summary += 1
    for i in range(summary):
        if i > 0 and t[i] == t[i-1] + 1:
            count += 1
        else:
            count = 1
        ans = max(ans, count)
    return ans

from random import randint


def the_longest_sequence():
    t = list()
    N = 100
    i = 1
    j = 1
    lastDifference = 1
    longestIncreasing = 1
    longestDecreasing = 1
    currentSequenceLength = 1
    for i in range(N):
        x = randint(1, N)
        if x not in t and x % 2 == 1:
            t.append(x)
        else:
            i -= 1
    print(t)
    while j < len(t):
        currentDifference = t[j] - t[j-1]
        if currentDifference == lastDifference:
            currentSequenceLength += 1
        else:
            currentSequenceLength = 2
            lastDifference = currentDifference
        if lastDifference > 0:
            longestIncreasing = max(longestIncreasing, currentSequenceLength)
        elif lastDifference < 0:
            longestDecreasing = max(longestDecreasing, currentSequenceLength)
        j += 1
        result = longestIncreasing - longestDecreasing
    return result


print(the_longest_sequence())

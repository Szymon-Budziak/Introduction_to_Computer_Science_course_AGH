from random import randint


def odd_number_check(N):
    t = [randint(1, 1001) for _ in range(N)]
    t2 = [a for a in t if all(int(b) % 2 == 1 for b in str(a))]
    for num in t2:
        copy_number = num
        while copy_number > 1:
            digit = copy_number % 10
            copy_number //= 10
            if digit % 2 != 0:
                continue
            else:
                break
        if copy_number == 1:
            return num
    return False


N = 1000
print(odd_number_check(N))

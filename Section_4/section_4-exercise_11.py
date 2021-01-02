from random import randint


def friends_numbers(array):
    result = 0
    for i in range(len(array)):
        for j in range(len(array)-1):
            number = array[i][j]
            copy_number = number
            str_number = str(number)
            for k in str_number:
                for m in str(array[i][j+1]):
                    if k == m:
                        number %= 10**(len(str_number)-1)
                        str_number = str(number)
                        break
            if number == 0 and copy_number > 0:
                result += 1
    return result


N = 5
array = [[randint(1, 100) for _ in range(N)]for _ in range(N)]
print(friends_numbers(array))

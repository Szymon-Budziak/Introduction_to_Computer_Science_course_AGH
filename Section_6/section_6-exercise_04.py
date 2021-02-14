# 1ST SOLUTION


def is_move_possible(x, y, array):
    if x >= 0 and y >= 0 and x < len(array) and y < len(array) and\
            array[x][y] == 0:
        return True
    return False


def solution(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end=" ")
        print()


def chess_horse(array):
    moves_counter = 1
    x_move = [2, 1, -1, -2, -2, -1,  1,  2]
    y_move = [1, 2,  2,  1, -1, -2, -2, -1]
    array[0][0] = 1
    if not(horse_tour(array, 0, 0, x_move, y_move, moves_counter)):
        return False
    else:
        solution(array)


def horse_tour(array, x, y, x_move, y_move, moves_counter):
    if moves_counter == len(array) ** 2:
        return True
    else:
        for i in range(8):
            new_x = x + x_move[i]
            new_y = y + y_move[i]
            if is_move_possible(new_x, new_y, array):
                array[new_x][new_y] = 1
                if horse_tour(array, new_x, new_y, x_move, y_move,
                              moves_counter+1):
                    return True
                array[new_x][new_y] = 0
        return False


# 2ND SOLUTION


def move_possible(array, i, x, y):
    x_move = [1, 2, 2, 1, -1, -2, -2, -1]
    y_move = [2, 1, -1, -2, -2, -1,  1,  2]
    new_x = x + x_move[i]
    new_y = y + y_move[i]
    if new_x >= 0 and new_y >= 0 and new_x < len(array) and new_y < len(array)\
            and array[new_y][new_x] == 0:
        return (new_x, new_y)
    return None


def horse_jump(array, x=0, y=0, counter=1):
    array[y][x] = counter
    if counter == len(array)**2:
        print_result(array)
        exit()
    for i in range(8):
        r = move_possible(array, i, x, y)
        if r is not None:
            horse_jump(array, r[0], r[1], counter+1)
    array[y][x] = 0


def print_result(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i][j], end="\t")
        print()


N = 6
array = [[0 for _ in range(N)] for _ in range(N)]
horse_jump(array)

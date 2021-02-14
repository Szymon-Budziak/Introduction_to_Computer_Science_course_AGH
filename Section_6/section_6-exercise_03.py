from random import randint


def chess_king(i, k, field_cost_result):
    field_cost_result += array[i][k]
    summary = -1
    if i == 7:
        return field_cost_result
    else:
        for x in range(k-1, k+2):
            if x >= 0 and x < 8:
                if summary == -1:
                    summary = chess_king(i+1, x, field_cost_result)
                else:
                    summary = min(chess_king(
                        i+1, x, field_cost_result), summary)
    return summary


k = randint(0, 7)
array = [[randint(1, 9) for _ in range(8)] for _ in range(8)]
print(chess_king(0, k, 0))

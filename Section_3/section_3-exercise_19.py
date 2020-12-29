def the_longest_summertree(array):
    array_len = len(array)
    result = 0
    max_result = 0
    length = 0
    max_length = 0
    index_summary = 0
    for i in range(array_len-1):
        if array[i] < array[i+1]:
            result += array[i]
            index_summary += i
            length += 1
            if result == index_summary and length > max_length:
                max_result = result
                max_length = length
        else:
            if array[i-1] < array[i]:
                result += array[i]
                index_summary += i
                length += 1
                if result == index_summary and length > max_length:
                    max_result = result
                    max_length = length
            result = 0
            index_summary = 0
            length = 0
    if i == array_len-2:
        if array[i+1] > array[i]:
            result += array[i+1]
            index_summary += i+1
            length += 1
            if result == index_summary and length > max_length:
                max_result = result
                max_length = length
    if max_result > 0 and max_length > 0:
        return max_result
    else:
        return 0


array = [0, 1, 2, 3, 4, 5, 545, 423, 312, 9, 10, 11, 12, 13, 14, 15, 16]
print(the_longest_summertree(array))

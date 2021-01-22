class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def base_convert(number):
    a = ""
    hex = "0123456789ABCDEF"
    while number > 0:
        a = hex[number % 8] + a
        number = number // 8
    return int(a)


def count_digits(number):
    five_count = 0
    while number != 0:
        c = number % 10
        number //= 10
        if c == 5:
            five_count += 1
    if five_count % 2 == 0:
        return True
    return False


def relocate_to_the_beginning(first):
    p = None
    q = first
    if first is None:
        return None
    converted_p = base_convert(q.value)
    flag = True
    while q is not None:
        if count_digits(converted_p):
            r = p
            if flag:
                r = q
            p = q
            q = p.next
            r.next = first
            first = r
        else:
            p = q
            q = p.next
        converted_p = base_convert(p.value)
        flag = False
    if p is not None:
        if count_digits(converted_p):
            r = p
            r.next = first
            first = r

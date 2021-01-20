class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


# 1ST SOLUTION ITERATION


def iteration_merge(p1, p2):
    f = Node()
    last = f
    while p1 is not None and p2 is not None:
        if p1.value < p2.value:
            last.next = p1
            last = p1
            p1 = p1.next
        else:
            last.next = p2
            last = p2
            p2 = p2.next
    if p1 is not None:
        last.next = p1
    else:
        last = p2
    return f.next


# 2ND SOLUTION RECURSION


def recursion_merge(p1, p2):
    if p1 is None:
        return p1
    if p2 is None:
        return p2
    if p1.value < p2.value:
        result = p1
        result.next = recursion_merge(p1.next, p2)
    else:
        result = p2
        result.next = recursion_merge(p1, p2.next)
    return result

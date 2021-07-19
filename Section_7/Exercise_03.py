"""
Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do funkcji należy
przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
- funkcja iteracyjna,
- funkcja rekurencyjna.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


def create_list(p):
    T = []
    while p is not None:
        T.append(p.value)
        p = p.next
    return T


# 1ST SOLUTION: ITERATION


def iteration_merge(p1, p2):
    new_node = Node(None)
    last = new_node
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
    return new_node.next


# 2ND SOLUTION: RECURSION


def recursion_merge(p1, p2):
    if p1 is None:
        return p2
    if p2 is None:
        return p1
    if p1.value < p2.value:
        result = p1
        result.next = recursion_merge(p1.next, p2)
    else:
        result = p2
        result.next = recursion_merge(p1, p2.next)
    return result


T1 = [1, 11, 19, 3, 5, 8, 2, 9]
ll1 = create_linked_list(T1)
T2 = [12, 7, 14, 18, 1, 6]
ll2 = create_linked_list(T2)
iteration = iteration_merge(ll1, ll2)
print(create_list(iteration))

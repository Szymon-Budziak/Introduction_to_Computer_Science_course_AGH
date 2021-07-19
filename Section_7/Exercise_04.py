"""
Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverse_list(L):
    if L is None:
        return None
    p = None
    q = L.next
    while L is not None:
        L.next = p
        p = L
        L = q
        if q is not None:
            q = q.next
    return p


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


T = [1, 6, 3, 24, 12, 7, 3, 18, 16]
ll = create_linked_list(T)
head = reverse_list(ll)
print(create_list(head))

"""
Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.
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


def increase_by_one(head):
    if head is None:
        return None
    new_head = reverse_list(head)
    current = new_head
    while current is not None:
        if current.value < 9:
            current.value += 1
            first = reverse_list(new_head)
            return first
        if current.value == 9:
            current.value = 0
            current = current.next
    if current is None:
        first = reverse_list(new_head)
        new_node = Node(1)
        new_node.next = first
        first = new_node
        return first


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


T = [1, 3, 7, 2, 5, 9]
ll = create_linked_list(T)
head = increase_by_one(ll)
print(create_list(head))

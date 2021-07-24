"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach
typu int, usuwającą wszystkie elementy, których wartość dzieli bez reszty wartość bezpośrednio
następujących po nich elementów.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_divisible_numbers(head):
    if head is None:
        return None
    current = head
    while current.next is not None:
        actual_value = current.value
        next_value = current.next.value
        if next_value % actual_value == 0:
            current.next = current.next.next
        else:
            current = current.next
    return head


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


T = [3, 6, 7, 21, 44, 2, 4, 8, 11]
ll = create_linked_list(T)
head = remove_divisible_numbers(ll)
print(create_list(head))

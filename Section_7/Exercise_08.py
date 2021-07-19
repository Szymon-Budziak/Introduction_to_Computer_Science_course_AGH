"""
Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi element listy. Do funkcji
należy przekazać wskazanie na pierwszy element listy.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_every_other(head):
    if head is None:
        return None
    current = head
    while current.next is not None and current.next.next is not None:
        current.next = current.next.next
        current = current.next
    if current.next is not None:
        current.next = None
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


T = [16, 11, 3, 8, 12, 31, 18, 11, 54]
ll = create_linked_list(T)
head = remove_every_other(ll)
print(create_list(head))

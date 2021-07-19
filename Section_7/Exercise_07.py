"""
Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji należy przekazać
wskazanie na pierwszy element listy.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_last_element(head):
    if head is None:
        return None
    previous = None
    current = head
    while current.next is not None:
        previous = current
        current = current.next
    previous.next = None
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


T = [3, 6, 8, 23, 9, 3, 43, 2, 18]
ll = create_linked_list(T)
head = remove_last_element(ll)
print(create_list(head))

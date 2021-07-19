"""
Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do funkcji należy przekazać
wskazanie na pierwszy element listy oraz wstawianą wartość.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def add_last_element(head, value):
    if head is None:
        head = Node(value)
        return head
    current = head
    while current.next is not None:
        current = current.next
    node = Node(value)
    current.next = node
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


T = [6, 24, 9, 45, 8, 1, 15]
ll = create_linked_list(T)
head = add_last_element(ll, 23)
print(create_list(head))

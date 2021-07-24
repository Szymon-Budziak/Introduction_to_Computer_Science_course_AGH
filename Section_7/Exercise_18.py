"""
Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy unikalne. Do funkcji należy
przekazać wskazanie na pierwszy element listy.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def only_unique(head):
    if head is None:
        return None
    if head.next is None:
        return head
    current = head
    previous = None
    while current is not None:
        actual = current
        next_actual = current.next
        flag = False
        while next_actual is not None:
            if next_actual.value == current.value:
                next_actual = next_actual.next
                flag = True
                if next_actual is None:
                    actual.next = None
            else:
                actual.next = next_actual
                actual = actual.next
                next_actual = next_actual.next
        if flag:
            current = current.next
            if previous is None:
                head = current
        else:
            if previous is None:
                previous = current
            else:
                previous.next = current
                previous = previous.next
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


T = [5, 23, 8, 34, 98, 34, 5, 5, 23, 23]
ll = create_linked_list(T)
head = only_unique(ll)
print(create_list(head))

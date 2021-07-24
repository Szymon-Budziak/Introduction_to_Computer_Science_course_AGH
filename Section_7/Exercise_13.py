"""
Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy element listy o wartościach
typu int, usuwającą wszystkie elementy, których wartość jest mniejsza od wartości bezpośrednio
poprzedzających je elementów.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_lesser_number(head):
    if head is None:
        return None
    current = head
    q = current.next
    while q is not None and q.next is not None:
        if current.value <= q.value:
            current = current.next
            q = current.next
        else:
            current.next = q.next
            current = current.next
            q = current.next
    if q is not None and current.value > q.value:
        current.next = None
        current = current.next
    elif q is not None and current.value <= q.value:
        current = current.next
        q = current.next
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


T = [2, 4, 7, 3, 5, 6, 11, 18, 4, 2, 1, 14]
ll = create_linked_list(T)
head = remove_lesser_number(ll)
print(create_list(head))

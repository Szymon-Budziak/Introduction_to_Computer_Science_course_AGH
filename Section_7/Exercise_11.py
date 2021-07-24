"""
Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do której przekazujemy wskaźnik
na początek oraz wartość klucza. Jeżeli element o takim kluczu występuje w liście należy go usunąć
z listy. Jeżeli elementu o zadanym kluczu brak w liście należy element o takim kluczu wstawić do listy.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_or_add_key(head, key):
    if head is None:
        return Node(key)
    if head.value == key:
        head = head.next
        return head
    current = head
    while current.next is not None:
        if current.next.value == key:
            current.next = current.next.next
            return head
        current = current.next
    current.next = Node(key)
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


T = [15, 18, 7, 68, 76, 12, 82, 2, 9]
ll = create_linked_list(T)
head = remove_or_add_key(ll, 5)
print(create_list(head))

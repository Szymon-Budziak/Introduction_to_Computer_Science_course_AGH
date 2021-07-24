"""
Dana jest lista, który być może zakończona jest cyklem. Napisać funkcję, która sprawdza ten fakt.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def detect_cycle(head):
    if head is None:
        return None
    current = head
    visited = []
    while current is not None:
        if current.value in visited:
            return True
        visited.append(current.value)
        current = current.next
    return False


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


T = [4, 8, 23, 98, 76, 234, 12, 71, 23]
ll = create_linked_list(T)
print(detect_cycle(ll))

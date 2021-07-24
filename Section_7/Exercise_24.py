"""
Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów przed cyklem.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def number_of_elements_before_cycle(head):
    if head is None:
        return None
    current = head
    visited = []
    starting_index = 0
    while current is not None:
        if current.value in visited:
            starting_index = visited.index(current.value)
            return starting_index
        else:
            visited.append(current.value)
        current = current.next
    return starting_index


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


T = [4, 8, 23, 98, 76, 234, 12, 71, 765, 98]
ll = create_linked_list(T)
print(number_of_elements_before_cycle(ll))

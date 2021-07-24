"""
Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def number_of_elements_in_cycle(head):
    if head is None:
        return None
    current = head
    visited = []
    actual_index = 0
    starting_index = None
    while current is not None:
        if current.value in visited:
            starting_index = visited.index(current.value)
            break
        else:
            visited.append(current.value)
        actual_index += 1
        current = current.next
    if starting_index is not None:
        length = actual_index - starting_index
        return length
    return False


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


T = [4, 8, 23, 98, 76, 234, 12, 71, 765, 98]
ll = create_linked_list(T)
print(number_of_elements_in_cycle(ll))

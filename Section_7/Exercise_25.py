"""
Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
ostatniego elementu przed cyklem.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def pointer_to_the_last_element(head):
    if head is None:
        return None
    current = head
    visited = []
    starting_index = None
    while current is not None:
        if current.value in visited:
            starting_index = visited.index(current.value)
            break
        else:
            visited.append(current.value)
        current = current.next
    if starting_index is None:
        return head
    current = head
    for i in range(starting_index - 1):
        current = current.next
    return current


def create_linked_list(T):
    p = None
    for i in range(len(T) - 1, -1, -1):
        q = Node(T[i])
        q.next = p
        p = q
    return p


T = [4, 8, 23, 98, 76, 234, 12, 71, 765, 98]
ll = create_linked_list(T)
print(pointer_to_the_last_element(ll))

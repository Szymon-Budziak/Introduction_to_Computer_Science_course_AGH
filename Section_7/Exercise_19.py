"""
Elementy w liście są uporządkowane według wartości klucza. Proszę napisać funkcję usuwającą z listy
elementy o nieunikalnym kluczu. Do funkcji przekazujemy wskazanie na pierwszy element listy,
funkcja powinna zwrócić liczbę usuniętych elementów.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_non_unique_elements(head):
    if head is None:
        return None
    current = head
    while current is not None and current.next is not None:
        if current.value == current.next.value:
            actual = current.next
            while actual is not None and actual.value == current.value:
                actual = actual.next
            current.next = actual
        else:
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


T = [3, 9, 9, 12, 18, 18, 18, 26, 26, 65, 80, 80, 93]
ll = create_linked_list(T)
head = remove_non_unique_elements(ll)
print(create_list(head))

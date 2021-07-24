"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy dwukierunkowej,
usuwa z niej wszystkie elementy, w których wartość klucza w zapisie binarnym ma nieparzystą
ilość jedynek.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


def count_ones(number):
    count = 0
    while number > 0:
        if number % 2 == 1:
            count += 1
        number //= 2
    if count % 2 == 1:
        return True
    return False


def remove_binary_numbers(head):
    if head is None:
        return None
    current = head
    while current is not None:
        if count_ones(current.value):
            if current.prev is None:
                head = current.next
                if current.next is not None:
                    current.next.prev = None
            else:
                current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
        current = current.next
    return head


def create_doubly_linked_list(T):
    p = None
    for i in range(len(T)):
        q = Node(T[i])
        p, q.next = q, p
        if q.next is not None:
            q.next.prev = q
    return p


def print_reversed_double_linked_list(head):
    T = []
    current = head
    while current.next is not None:
        current = current.next
    while current is not None:
        T.append(current.value)
        current = current.prev
    return T


T = [7, 32, 3, 2, 42, 78, 34, 84, 19, 6]
ll = create_doubly_linked_list(T)
head = remove_binary_numbers(ll)
print(print_reversed_double_linked_list(head))

"""
Kolejne elementy listy o zwiększającej się wartości pola val nazywamy podlistą rosnącą. Proszę
napisać funkcję, która usuwa z listy wejściowej najdłuższą podlistę rosnącą. Warunkiem usunięcia
jest istnienie w liście dokładnie jednej najdłuższej podlisty rosnącej.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_the_longest_sublist(head):
    if head is None:
        return None
    current = head
    previous = None
    actual_length = best_length = 1
    actual_indexes = None
    starting_index = ending_index = None
    flag = True
    while current.next is not None:
        if actual_length == 1:
            actual_indexes = (previous, current)
        if current.next.value >= current.value:
            actual_length += 1
        else:
            if actual_length == best_length:
                flag = False
            elif actual_length > best_length:
                best_length = actual_length
                starting_index = actual_indexes[0]
                ending_index = actual_indexes[1]
                flag = True
            actual_length = 1
        previous = current
        current = current.next
    if actual_length > best_length:
        best_length = actual_length
        starting_index = actual_indexes[0]
        ending_index = actual_indexes[1]
        flag = True
    if flag:
        while best_length > 0 and ending_index is not None:
            starting_index.next = ending_index.next
            ending_index = ending_index.next
            best_length -= 1
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


T = [3, 6, 1, 4, 8, 12, 17, 24, 3, 5, 9, 17, 28]
ll = create_linked_list(T)
head = remove_the_longest_sublist(ll)
print(create_list(head))

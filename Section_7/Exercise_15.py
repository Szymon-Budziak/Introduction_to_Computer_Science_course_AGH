"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy
jednokierunkowej, usuwa z niej wszystkie elementy, w których wartość klucza w zapisie
trójkowym ma większą ilość jedynek niż dwójek.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def base_convert(number):
    count = [0] * 3
    while number > 0:
        count[number % 3] += 1
        number //= 3
    if count[1] > count[2]:
        return True
    return False


def remove_key_elements(head):
    if head is None:
        return None
    current = head
    while current.next is not None:
        actual_value = current.next.value
        if base_convert(actual_value):
            current.next = current.next.next
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


T = [2, 10, 12, 1, 5, 11, 14, 6, 3]
ll = create_linked_list(T)
head = remove_key_elements(ll)
print(create_list(head))

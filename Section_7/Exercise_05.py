"""
Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do 10 list, według ostatniej
cyfry pola value. W drugim kroku powstałe listy należy połączyć w jedną listę odsyłaczową, która
jest posortowana niemalejąco według ostatniej cyfry pola val.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def add_element(array, value):
    new_node = Node(value)
    if len(array) == 0:
        array.append(new_node)
        return
    node = array[0]
    while node.next is not None:
        node = node.next
    node.next = new_node
    array.append(new_node)


def split(head):
    digits = [[] for _ in range(10)]
    while head is not None:
        last = head.value % 10
        add_element(digits[last], head.value)
        head = head.next
    array = Node(None)
    for i in range(10):
        if len(digits[i]) > 0:
            if array.value is None and array.next is None:
                array.next = digits[i][0].next
                array.value = digits[i][0].value
            else:
                current = array
                while current.next is not None:
                    current = current.next
                current.next = digits[i][0]
    return array


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


T = [9, 1, 8, 4, 2, 18, 59, 1, 16, 11, 23, 85, 74, 27]
ll = create_linked_list(T)
head = split(ll)
print(create_list(head))

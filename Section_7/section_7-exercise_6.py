class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def add_last_element(first, value):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None:
        p = q
        q = p.next
    if q is None:
        q = Node(value)
        first = q
        q = first.next
    return first.value


elem3 = Node(5)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)
print(add_last_element(elem1, 23))

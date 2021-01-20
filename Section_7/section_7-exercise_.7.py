class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_last_element(first):
    p = first
    q = p.next
    if p is None:
        return None
    r = q.next
    while r is not None:
        p = q
        q = r
        r = q.next
    q = None
    p.next = r
    return p.value


elem3 = Node(5)
elem2 = Node(4, elem3)
elem1 = Node(1, elem2)
print(remove_last_element(elem1))

class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def reverse_list(a):
    if a is None:
        return None
    if a.next is None:
        return None
    p = None
    q = a
    r = a.next
    while q is not None:
        q.next = p
        p = q
        q = r
        if r is not None:
            r = r.next

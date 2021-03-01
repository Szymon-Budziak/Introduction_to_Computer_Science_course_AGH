class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def reverse_list(L):
    if L is None:
        return None
    p = None
    q = L.next
    while L is not None:
        L.next = p
        p = L
        L = q
        if q is not None:
            q = q.next
    return p

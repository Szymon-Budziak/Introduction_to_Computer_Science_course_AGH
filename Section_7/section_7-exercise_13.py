class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_lesser_number(first):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None and q.next is not None:
        if p.value <= q.value:
            p = p.next
            q = p.next
        else:
            p.next = q.next
            p = p.next
            q = p.next
    if q is not None and p.value > q.value:
        p.next = None
        p = p.next
    elif q is not None and p.value <= q.value:
        p = p.next
        q = p.next

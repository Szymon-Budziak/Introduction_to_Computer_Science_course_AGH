class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def remove_divisible_numbers(first):
    p = first
    q = p.next
    if p is None:
        return None
    while q is not None and q.next is not None:
        if q.value % p.value == 0:
            p = p.next
            q = p.next
        else:
            p.next = q.next
            p = p.next
            q = p.next
    if q is not None and q.value % p.value != 0:
        p.next = None
        p = p.next
    elif q is not None and q.value % p.value == 0:
        p = p.next
        q = p.next

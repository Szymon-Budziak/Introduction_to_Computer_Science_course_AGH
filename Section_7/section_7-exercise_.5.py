class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def split(head):
    first = [None for _ in range(10)]
    last = [None for _ in range(10)]
    while head is not None:
        c = head.value % 10
        if first[c] is None:
            first[c] = last[c] = head
        else:
            last[c].next = head
            last[c] = last[c].next
        head = head.next

    array = None
    for i in range(9, -1, -1):
        if first[i] is not None:
            last[i].next = array
            array = array[i]
    return array

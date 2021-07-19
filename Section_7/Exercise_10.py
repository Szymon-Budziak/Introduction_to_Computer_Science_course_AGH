"""
Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą dwie
takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


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


def add(node, value):
    if node is None:
        return Node(value)
    while node.next is not None:
        node = node.next
    node.next = Node(value)


def add_two_numbers(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1
    new_head1 = reverse_list(head1)
    new_head2 = reverse_list(head2)
    p = new_head1
    q = new_head2
    new_list = Node(None)
    total_value = 0
    while p is not None or q is not None:
        actual_value = total_value
        if p is not None:
            actual_value += p.value
            p = p.next
        if q is not None:
            actual_value += q.value
            q = q.next
        total_value = actual_value // 10
        add(new_list, actual_value % 10)
    if total_value != 0:
        add(new_list, total_value)
    if new_list.value is None:
        new_list = new_list.next
    first = reverse_list(new_list)
    return first


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


T1 = [1, 6, 2, 4]
T2 = [4, 3, 7]
ll1 = create_linked_list(T1)
ll2 = create_linked_list(T2)
head = add_two_numbers(ll1, ll2)
print(create_list(head))

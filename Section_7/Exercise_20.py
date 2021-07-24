"""
Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów. Krańce przedziałów określa
uporządkowana para liczb całkowitych. Proszę napisać stosowne deklaracje oraz funkcję redukującą
liczbę elementów listy. Na przykład lista: [[15,19], [2,5], [7,11], [8,12], [5,6], [13,17]],
powinien zostać zredukowany do listy: [[13,19], [2,6], [7,12]]
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def reduce_number_of_elements(head):
    if head is None:
        return None
    curr = head
    nd = None
    start = None
    while curr is not None:
        flag = True
        while nd is not None:
            if (nd.value[0] <= curr.value[0] <= nd.value[1] or nd.value[0] <= curr.value[1] <= nd.value[1]) or \
                    (curr.value[0] <= nd.value[0] <= curr.value[1] or curr.value[0] <= nd.value[1] <= curr.value[1]):
                if curr.value[0] <= nd.value[0]:
                    nd.value[0] = curr.value[0]
                if curr.value[1] >= nd.value[1]:
                    nd.value[1] = curr.value[1]
                flag = False
                break
            nd = nd.next
        if flag:
            new_node = Node(curr.value)
            if start is None:
                start = new_node
            else:
                actual = start
                while actual.next is not None:
                    actual = actual.next
                actual.next = new_node
        curr = curr.next
        nd = start
    return start


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


T = [[15, 19], [2, 5], [7, 11], [8, 12], [5, 6], [13, 17]]
ll = create_linked_list(T)
head = reduce_number_of_elements(ll)
print(create_list(head))

"""
Proszę napisać funkcję, która otrzymując jako parametr wskazujący na początek listy jednokierunkowej,
przenosi na początek listy te z nich, które mają parzystą ilość piątek w zapisie ósemkowym.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def count_number_of_5s(number):
    count = 0
    while number > 0:
        if number % 8 == 5:
            count += 1
        number //= 8
    if count % 2 == 0:
        return True
    return False


def add_at_the_beginning(head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head


def relocate_to_the_beginning(head):
    if head is None:
        return None
    current = head
    while current is not None and current.next is not None:
        actual_value = current.next.value
        if count_number_of_5s(actual_value):
            head = add_at_the_beginning(head, actual_value)
            current.next = current.next.next
        else:
            current = current.next
    return head


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


T = [41, 7, 23, 76, 5, 19, 13, 54, 21]
ll = create_linked_list(T)
head = relocate_to_the_beginning(ll)
print(create_list(head))

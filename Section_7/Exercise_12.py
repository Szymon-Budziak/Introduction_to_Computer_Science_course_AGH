"""
Zbiór mnogościowy zawierający napisy jest reprezentowany w postaci jednokierunkowej listy.
Napisy w łańcuchu są uporządkowane leksykograficznie. Proszę napisać stosowne definicje typów
oraz funkcję dodającą napis do zbioru. Do funkcji należy przekazać wskaźnik do listy oraz
wstawiany napis, funkcja powinna zwrócić wartość logiczną wskazującą, czy w wyniku operacji
moc zbioru uległa zmianie.
"""


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


def string_comparison(string1, string2):
    for i in range(min(len(string1), len(string2))):
        if ord(string1[i]) < ord(string2[i]):
            return True
        elif ord(string1[i]) > ord(string2[i]):
            return False


def add_string(head, string):
    current = head
    previous = Node()
    previous.next = current
    actual, new_node = previous, Node(string)
    if current is not None and string_comparison(string, current.value):
        previous.next = new_node
        new_node.next = current
        return actual.next
    while current is not None:
        if string_comparison(string, current.value):
            previous.next = new_node
            new_node.next = current
            return actual.next
        previous = current
        current = current.next
    previous.next = new_node
    return actual.next


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


T = ["abcef", "bfij", "klow", "pruz", "ywz"]
ll = create_linked_list(T)
head = add_string(ll, "cuw")
head = add_string(head, "aaaa")
head = add_string(head, "rt")
print(create_list(head))

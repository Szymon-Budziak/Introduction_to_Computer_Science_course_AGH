"""
Zastosowanie listy odsyłaczowej do implementacji tablicy rzadkiej. Proszę napisać trzy funkcje:
– inicjalizującą tablicę,
– zwracającą wartość elementu o indeksie n,
– podstawiającą wartość value pod indeks n.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        node = self.head
        if node is not None:
            new_node = Node(data)
            new_node.next = node
            self.head = new_node
            return
        self.head = Node(data)

    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def add_index(self, data, index):
        if index < 0 or index > self.length():
            print("Wrong index")
            return False
        if index == 0:
            self.add_at_beginning(data)
            return
        actual_idx = 0
        current = self.head
        while current is not None:
            if actual_idx == index - 1:
                node = Node(data)
                node.next = current.next
                current.next = node
                return
            current = current.next
            actual_idx += 1

    def remove_index(self, index):
        if index < 0 or index >= self.length():
            print("Wrong index")
            return
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        current = self.head
        while current is not None:
            if count == index - 1:
                current.next = current.next.next
                break
            current = current.next
            count += 1

    def display_result(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value) + "->"
            current = current.next
        print(result)


ll = LinkedList()
ll.add_index(2, 0)
ll.add_index(3, 1)
ll.add_index(11, 2)
ll.remove_index(2)
ll.remove_index(0)
ll.add_index(15, 0)
ll.add_index(12, 2)
ll.display_result()

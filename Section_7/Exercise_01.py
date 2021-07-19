"""
Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze struktury listy odsyłaczowej.
- czy element należy do zbioru,
- wstawienie elementu do zbioru,
- usunięcie elementu ze zbioru.
"""
from collections import deque


# 1ST SOLUTION


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_element_in(self, data):
        if self.head is None:
            return "List is empty"
        node = self.head
        while node is not None:
            if node.value == data:
                return True
            node = node.next
        return False

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        node = self.head
        while node.next is not None:
            node = node.next
        node.next = Node(data)

    def remove(self, data):
        if self.head is None:
            print("Linked list is empty")
            return
        previous = None
        current = self.head
        while current is not None and current.value != data:
            previous = current
            current = current.next
        if current is None:
            return self.head
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def display_result(self):
        if self.head is None:
            print("Linked list is empty")
            return
        i = self.head
        result = ''
        while i is not None:
            result += str(i.value) + "->"
            i = i.next
        print(result)


# 2ND SOLUTION USING DEQUE


linked_list = deque([1, 2, 3, 4, 5, 6])


def add_last_element(element, l_list=linked_list):
    l_list.append(element)
    return l_list


def remove_last_element(element, l_list=linked_list):
    l_list.pop()
    return l_list


def add_first_element(element, l_list=linked_list):
    l_list.appendleft(element)
    return l_list


def remove_first_element(element, l_list=linked_list):
    l_list.popleft()
    return l_list


ll = LinkedList()
ll.add(5)
ll.add(7)
ll.add(15)
ll.remove(15)
ll.add(17)
ll.add(11)
ll.remove(7)
ll.display_result()
print(ll.is_element_in(2))
print(ll.is_element_in(5))

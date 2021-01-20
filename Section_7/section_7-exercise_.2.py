from random import randint


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_beginning(self):
        node = Node(randint(1, 10), self.head)
        self.head = node
        print(node.value)

    def display_element(self, index, length):
        if self.head is None:
            print("List is empty")
            return
        if index < 0 or index >= length:
            return False
        count = 0
        i = self.head
        while i is not None:
            if count == index:
                return i.value
            i = i.next
            count += 1

    def substitute_element(self, variable, index, length):
        if index < 0 or index >= length:
            return False
        i = self.head
        count = 0
        while i is not None:
            if count == index:
                i.value = variable
                break
            i = i.next
            count += 1

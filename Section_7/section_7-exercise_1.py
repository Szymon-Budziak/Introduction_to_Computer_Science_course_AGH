from collections import deque


# 1ST SOLUTION


class Node:
    def __init__(self, number=None, next_node=None):
        self.value = number
        self.next = next_node


class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(number=nodes.pop(0))
            self.head = node
            for element in nodes:
                node.next = Node(number=element)
                node = node.next

    def is_element_in(self, element):
        if self.head is None:
            return "List is empty"
        node = self.head
        while node is not None:
            if node == element:
                return True
        return False

    def add_element(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first_element(self, node):
        node.next = self.head
        self.head = node

    def add_last_element(self, node):
        if not self.head:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_element_after(self, current_node, new_node):
        if not self.head:
            return "List is empty!"
        for node in self:
            if node.value == current_node:
                new_node.next = node.next
                node.next = new_node
                return
        if self.nodes == []:
            return False

    def remove_node(self, target_node):
        if not self.head:
            return "List is empty"
        if self.head.value == target_node:
            self.head = self.head.next
            return
        previous_node = self.head
        for node in self:
            if node.value == target_node:
                previous_node.next = node.next
                return
            previous_node = node
        return False


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


# 3RD SOLUTION


class LinkedList2:
    def __init__(self):
        self.head = None

    def add_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

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

    def add_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        i = self.head
        while i.next is not None:
            i = i.next
        i.next = Node(data, None)

    def length(self):
        count = 0
        i = self.head
        while i is not None:
            count += 1
            i = i.next
        return count

    def remove_index(self, index):
        if index < 0 or index >= self.length():
            return False
        if index == 0:
            self.head - self.head.next
            return
        count = 0
        i = self.head
        while i is not None:
            if count == index-1:
                i.next = i.next.next
                break
            i = i.next
            count += 1

    def add_index(self, index, data):
        if index < 0 or index >= self.length():
            return False
        if index == 0:
            self.add_at_beginning(data)
            return
        count = 0
        i = self.head
        while i is not None:
            if count == index-1:
                node = Node(data, i.next)
                i.next = node
                break
            i = i.next
            count += 1


ll = LinkedList2()
ll.add_at_beginning(72)
ll.add_at_end(31)
ll.add_at_end(2)
ll.remove_index(1)
ll.add_index(1, 5665)
ll.display_result()

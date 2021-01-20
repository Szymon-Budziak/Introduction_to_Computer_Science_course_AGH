class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next = next_node


def add_string(first, string):
    p = first
    q = p.next
    string = ''.join(sorted(string))
    change = False
    while q is not None:
        insert = False
        for i in range(len(string)):
            if q.value > string[i] and p.value != string[i]:
                r = Node(string[i])
                p.next = r
                r.next = q
                p = r
                p.next = q
                insert = True
                string = string.replace(string[i], "", 1)
                change = True
                break
            elif q.value > string[i] and string[i] == p.value:
                string = string.replace(string[i], "", 1)
                insert = True
                break
        if not insert:
            p = q
            q = p.next
    if change:
        return True
    return False

class Node:
    def __init__(self, value=None, next_node = None):
        self.value = value
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def add_to_head(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
        # new node is both the head and the tail of the empty LL
        self.head = new_node
        self.tail = new_node
    else:
        # new node should point to the current head
        new_node.next_node = self.head
        # move head to the next node
        self.head = new_node

def add_to_tail(self, value):
    new_node = Node(value)
    if self.head is None and self.tail is None:
        new_tail = Node(value, None)
        # new node is both the head and the tail of the empty LL
        self.head = new_node
        self.tail = new_node
    else:
        # node at current tail will now point to the new node
        self.tail.next_node = new_node
        # tail will now point to the new node
        self.tail = new_node

def remove_head(self):
    # if LL is empty then return 'None'
    if not self.head:
        return None
    # if LL has 1 element only
    if self.head.next_node is None:
        current_value = self.head.value
        self.head = None
        self.tail = None
        return current_value
    else:
        current_value = self.head.value
        # head will point the node next to the current node
        self.head = self.head.next_node
        return current_value

def contains(self, value):
    # if LL is empty then return 'None'
    if self.head is None:
        return None
    # create node for the value
    current_node = self.head
    # loop through each node until we find the value or if the LL runs out
    while current_node != None:
        if current_node.value == value:
            return True
        current_node = current_node.next_node
    return False


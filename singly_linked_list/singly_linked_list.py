class Node:
    def __init__(self, value=None, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            # new node is both the head and the tail of the empty LL
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to the current head
            new_node.next = self.head
            # move head to the next node
            self.head = new_node

    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)
            # new node is both the head and the tail of the empty LL
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            self.tail = new_tail
            self.length += 1

    def remove_head(self):
        # if LL is empty then return 'None'
        if not self.head:
            return None
        # if LL has 1 element only
        if self.head.next is None:
            current_value = self.head.value
            self.head = None
            self.tail = None
            return current_value
        else:
            current_value = self.head.value
            # head will point the node next to the current node
            self.head = self.head.next
            return current_value

    def remove_tail(self):
        if self.tail is None:
            return None
        elif self.tail == self.head:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.length -= 1
            return current_tail.value
        else:
            current_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next
            current_tail = self.tail
            self.tail = current_node
            current_node.next = None
            self.length -= 1
            return current_tail.value

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
            current_node = current_node.next
        return False


class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = None

    def insert_data(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = node
            return

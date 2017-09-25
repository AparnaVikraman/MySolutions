class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class List:
    def __init__(self, node=None):
        self.head = node

    def insertnode(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = Node(data)

    def printlist(self, node):
        if node is not None:
            print(node.data)
            self.printlist(node.next)

    def get_length(self):
        node = self.head
        count = 0
        while node:
            count += 1
            node = node.next
        return count


#import pdb
#pdb.set_trace()
#l = List()
#l.insertnode(2)
#l.insertnode(3)
#l.printlist(l.head)

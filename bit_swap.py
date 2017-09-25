class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.nextnode = next_node

class LinkedList:
    def __init__(self):
        self.headnode = None
        self.newnode = Node(None, None)

    def insertdata(self, data):
        newnode = Node(data, None)
        if self.headnode is None:
            self.headnode = Node(None, None)
            self.headnode.nextnode = newnode
        else:
            self.newnode.nextnode = newnode

        self.newnode = newnode

    def bit_swap(self):
        import pdb
        pdb.set_trace()
        node = self.headnode.nextnode
        while node != None:
            tmpdata = node.data
            node.data = node.nextnode.data
            node.nextnode.data = tmpdata
            node = node.nextnode.nextnode

    def print_list(self):
        node = self.headnode
        while node != None:
            print node.data
            node = node.nextnode

user_input = input("Enter the num:")
print type(user_input)
binary = '{0:08b}'.format(user_input)
binary = list(binary)
l = LinkedList()
for x in binary:
    l.insertdata(x)
l.print_list()
l.bit_swap()
l.print_list()            

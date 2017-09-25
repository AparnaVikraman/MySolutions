class Node:
    def __init__(self, data, nextnode):
        self.data = data
        self.nextnode = nextnode

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

    def insertmiddle(self, data, location):
        newnode = Node(data, None)
        node = self.headnode
        for x in range(0,location-1):
           if node.nextnode is not None:
               node = node.nextnode
           else:
               self.insertlast(data)
               return
        tmp = node.nextnode
        newnode.nextnode = tmp
        node.nextnode = newnode

    def insertlast(self, data):
        node = self.headnode
        while(node.nextnode is not None):
            node = node.nextnode
        newnode = Node(data, None)
        node.nextnode = newnode

    def deletebylocation(self, location):
        node = self.headnode.nextnode
        for x in range(0,location-1):
            if node.nextnode is not None:
                node = node.nextnode
            else:
                print("Not in the limit")
                return
        node.nextnode = node.nextnode.nextnode

    def deletebydata(self, data):
        node = self.headnode
        while(node.nextnode != None and node.nextnode.data != data):
            node = node.nextnode
        if node.nextnode !=None:
            node.nextnode = node.nextnode.nextnode
        else:
            print("data not found")

    def printdata(self):
        node = self.headnode.nextnode
        while(node.nextnode is not None):
            print(node.data)
            node = node.nextnode
        print(node.data)

listt = [1,2,3,4,5]
l = LinkedList()
for x in range(0,5):
    l.insertdata(listt[x])
l.printdata()
print("insert middle")
a = input('value : ')
b = input('position : ')
l.insertmiddle(a, b)
l.printdata()
print("insert last")
a = input('value : ')
l.insertlast(a)
l.printdata()
print("delete by location")
a = input('location : ')
l.deletebylocation(a)
l.printdata()
print("delete by data")
a = input('value : ')
l.deletebydata(a)
l.printdata()

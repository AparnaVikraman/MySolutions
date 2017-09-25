class TrieNode():
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False

class Trie():

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def get_index(self, char):
        return ord(char) - ord('a')

    def insert(self, key):
        node = self.root
        for x in range(len(key)):
            index = self.get_index(key[x])
            if not node.children[index]:
                node.children[index] = self.getNode()
            else:
                if len(key) - 1 == x:
                    return False
            if node.isLeaf:
                return False
            node = node.children[index]
        node.isLeaf = True
        return True

    def search(self, key):
        node = self.root
        for x in range(len(key)):
            index = self.get_index(key[x])
            if not node.children[index]:
                return False
            node = node.children[index]
        #return node != None and node.isLeaf
        if node != None and node.isLeaf:
            return True
        else:
            return False

n = int(input())
s = []
trie = Trie()
for i in range(n):
    s = raw_input()
    check = trie.insert(s)
    if not check:
        print('BAD SET')
        print(s)
        break
if check:
    print('GOOD SET')

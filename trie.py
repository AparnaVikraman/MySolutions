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
            node = node.children[index]
        node.isLeaf = True

    def search(self, key):
        node = self.root
        for x in range(len(key)):
            index = self.get_index(key[x])
            if not node.children[index]:
                return False
            node = node.children[index]
        #return node != None and node.isLeaf
        if node != None and node.isLeaf:
            print("Found the word '"+key+"'")
        else:
            print("Not found")
    
    def _get_children(self, pattern, node):
        for x in range(26):
            #print("ss "+pattern)
            child = node.children[x]
            if child:
                pattern1 = pattern + chr(x+97)
                if child.isLeaf:
                    print(pattern1)
                self._get_children(pattern1, child)

    def get_pattern(self, key):
        node = self.root
        for x in range(len(key)):
            index = self.get_index(key[x])
            if not node.children[index]:
                print("Pattern not found")
                return
            node = node.children[index]
        result = []
        self._get_children(key, node)

def main():
    print("1.Add words 2.Search 3.Exit")
    n = int(raw_input())
    trie = Trie()
    options = {1: trie.insert,
               2: trie.search,
               3: trie.get_pattern}
    while(n<4):
        print("Enter key: ")
        key = raw_input()
        options[n](key)
        print("1.Add words 2.Search 3.Pattern 4.Exit")
        n = int(raw_input())
    #keys = ['are', 'ate', 'a', 'the', 'there', 'take', 'hello', 'help', 'hate', 'heels', 'heel']
    #for key in keys:
    #    trie.insert(key)
    #print trie.search('the')
    #trie.get_pattern('he')

if __name__ == '__main__':
    main()

class StackNode():
    def __init__(self, val, curmax=0):
        self.val = val
        self.curmax = curmax

class Stack():
    def __init__(self):
        self.top = -1
        self.node = []
        self.max = 0

    def isempty(self):
        return self.top == -1

    def push(self, val):
        self.top += 1
        if self.max < val:
            self.max = val
        self.node.append(StackNode(val, self.max))

    def pop(self):
        if not self.isempty():
            delnode = self.peek()
            del self.node[self.top]
            self.top -= 1
            if delnode.val == self.max:
                if self.isempty():
                    self.max = 0
                else:
                    self.max = self.peek().curmax

    def peek(self):
        if not self.isempty():
            return self.node[self.top]

if __name__ == '__main__':
    n = int(input())
    stack = Stack()
    for i in range(n):
        choice = input().strip()
        if len(choice) > 1:
            choice, val = choice.split(' ')
            choice, val = int(choice), int(val)
        else:
            choice = int(choice)
        if choice == 1:
            stack.push(val)
        elif choice == 2:
            stack.pop()
        elif choice == 3:
            print(stack.peek().curmax)

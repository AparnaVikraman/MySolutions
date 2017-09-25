import sys
import linkedlist

def push(result, sum):
    node = linkedlist.Node(sum)
    node.next = result
    return node

def addCarry(result, carry, a, temp):
    if a is not temp:
        result, carry = addCarry(result, carry, a.next, temp)
        sum = a.data + carry
        carry = sum/10
        sum = sum%10
        result = push(result, sum)
        return result, carry
    
def add_same_size(a, b, carry):
    if not a:
        return None

    result = linkedlist.Node()
    result.next, carry = add_same_size(a.next, b.next, carry)
    sum = a.data + b.data + carry
    carry = sum / 10
    result.data =  sum%10
    return result, carry

def add_numbers(a,b):
    if not a.head:
        return b.head
    if not b.head:
        return a.head

    n1 = a.get_length()
    n2 = b.get_length()
    if n1 == n2:
        result, carry = add_same_size(a.head, b.head, 0)
    else:
        size = abs(n1-n2)
        if n1 < n2:
            a, b = b, a
        temp = a.head
        for i in range(size):
            temp = temp.next

        result,carry = add_same_size(temp, b.head, 0)
        result, carry = addCarry(result, carry, a.head, temp)
    if not carry:
        result = push(result, carry)
    return result
    

a = sys.argv[1]
b = sys.argv[2]
l1 = linkedlist.List()
l2 = linkedlist.List()
for i in str(a):
    l1.insertnode(int(i))

for i in str(b):
    l2.insertnode(int(i))

result = add_numbers(l1, l2)
while result:
    print(result.data)
    result = result.next

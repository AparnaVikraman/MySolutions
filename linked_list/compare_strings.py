import linkedlist

def compare_strings(l,l1):
    while l and l1 and l.data == l1.data:
        l = l.next
        l1 = l1.next
    while l and l1:
        return 1 if l.data > l1.data else -1
    if l and not l1:
        return 1
    if not l and l1:
        return -1
    return 0
    
l = linkedlist.List()
s = "geekab"
for i in s:
    l.insertnode(i)

l1 = linkedlist.List()
s1 = "geeks"
for i in s1:
    l1.insertnode(i)

#l.printlist(l.head)
#l1.printlist(l1.head)
print(compare_strings(l.head,l1.head))

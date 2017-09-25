import re
string = raw_input("Enter the string: ")
print string
print len(string)
#print type(string)
#st = [ x for x in raw_input().split()]
#print len(st)
print any(c.isalpha() for c in string)
#for x in range(len(string)):
#    if x 

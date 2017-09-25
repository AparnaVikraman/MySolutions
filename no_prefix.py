"""
Given  strings. Each string contains only lowercase letters from (both inclusive). The set of  strings is said to be GOOD SET if no string is prefix of another string else, it is BAD SET. (If two strings are identical, they are considered prefixes of each other.)

For example, aab, abcde, aabcd is BAD SET because aab is prefix of aabcd.

def no_prefix(s, n):
    for i in range(1,n):
        for j in range(0, i):
            if s[j] in s[i][0:len(s[j])]:
                print("BAD SET")
                print(s[i])
                return
    print('GOOD SET')

if __name__ == '__main__':
    n = int(raw_input())
    s = []
    for i in range(n):
       s.append(raw_input())
    import pdb
    pdb.set_trace()
    no_prefix(s, n)

"""

def no_prefix(s, n):
    for i in range(1,n):
        for j in range(0, i):
            #if s[j] in s[i][0:j_len] or s[i] in s[j][0:i_len]:
            if s[i].startswith(s[j]) or s[j].startswith(s[i]):
                print("BAD SET")
                print(s[i])
                return
    print('GOOD SET')
    
n = int(input())
s = []
for i in range(n):
    s.append(input())
no_prefix(s,n)

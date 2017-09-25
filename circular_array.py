
n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in raw_input().strip().split(' ')]
rot = n % 5
result = [None]*n
for i in range(n):
    idx = (i+k)%n
    result[idx] = a[i]
for a0 in range(q):
    m = int(raw_input().strip())   
    print(result[m])


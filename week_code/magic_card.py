import math

def sum_sqrt(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + math.sqrt(arr[i])
    return int(sum)

def magic_card(arr, arr_back, i, n):
     if i==n:
         return 0
     return max(sum_sqrt(arr[i])+magic_card(arr, arr_back,i+1,n),
                sum_sqrt(arr_back[i])+magic_card(arr, arr_back,i+1,n))
    

if __name__ == '__main__':
    n, m, q = input().strip().split(' ')
    n, m, q = [int(n), int(m), int(q)]
    arr = []
    for i in range(n):
        a = list(map(int, input().strip().split(' ')))
        del a[0]
        arr.append(a)

    arr_back = []
    for i in range(n):
        s = set(range(m+1))-set(arr[i])
        arr_back.append(list(s))

    print(magic_card(arr, arr_back, 0, n))

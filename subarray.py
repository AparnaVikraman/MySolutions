if __name__ == '__main__':
    n = int(raw_input())
    arr = list(map(int, raw_input().strip().split(' ')))
    subarr = []
    for i in range(n+1):
       for j in range(i,n+1):
           ar = []
           for k in range(i,j):
               ar.append(arr[k])
           if ar and len(ar) > 1:
               subarr.append(ar)
    print subarr

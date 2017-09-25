def count(arr, x, y):
    countx=0
    county=0
    for i in range(len(arr)):
        if arr[i] == x:
            countx+=1
        elif arr[i] == y:
            county+=1
    return countx, county

if __name__ == '__main__':
    n, q = input().strip().split(' ')
    n, q = [int(n), int(q)]
    arr = list(map(int, input().strip().split(' ')))
    subarr = []
    for i in range(n+1):
       for j in range(i,n+1):
           ar = []
           for k in range(i,j):
               ar.append(arr[k])
           if ar:
               subarr.append(ar)
    for a0 in range(q):
        x, y = input().strip().split(' ')
        x, y = [int(x), int(y)]
        countnum=0
        for i in range(len(subarr)):
            cx,cy = count(subarr[i], x, y)
            if cx == cy:
                countnum+=1
        print(countnum)

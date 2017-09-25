def find_sum(x):
    sum = 0
    for i in x:
        sum = sum + int(i)
    return sum

def onceInATram(x):
    x = x + 1
    num = str(x)
    num = [num[:3], num[3:]]
    while find_sum(num[0]) != find_sum(num[1]):
        x = x + 1
        num = str(x)
        num = [num[:3], num[3:]]
    return x
   
if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print(result)

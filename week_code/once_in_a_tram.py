import sys

def recs_last(diff, num):
    num = list(num)
    if not num:
        return
    idx = len(num)-1
    old = int(num[idx])
    if int(num[idx])+diff > 9:
        num[idx] = '9'
    else:
        num[idx] = str(int(num[idx])+diff)
        return num    
    s = num.pop()
    num1 = recs_last(diff-9+old, ''.join(num))
    num1.append(s)
    return num1

def onceInATram(ticket):
    x = str(ticket)
    num = [x[:3], x[3:]]
    sum1 = 0; sum2 = 0
    for x in num[0]:
        sum1 =  sum1 + int(x)
    for y in num[1]:
        sum2 =  sum2 + int(y)
    if sum1 > sum2:
        diff =  abs(sum1 - sum2)
        num[1] = ''.join(recs_last(diff, num[1]))
        return ''.join(num)
    elif sum1 < sum2:
        num[0] = str(int(num[0]) + 1)
        num[1] = '000'
        sum1 = 0
        for x in num[0]:
            sum1 =  sum1 + int(x)
        num[1] = ''.join(recs_last(sum1, num[1]))
        return ''.join(num)
    else:
        ticket = ticket+1
        return onceInATram(ticket)

if __name__ == "__main__":
    x = int(raw_input().strip())
    result = onceInATram(x)
    print(result)


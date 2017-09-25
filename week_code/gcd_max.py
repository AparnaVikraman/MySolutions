import sys

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
def maximumGcdAndSum(a, b, n):
    # Complete this function
    gcd1 = []
    sum1 = []
    for i in range(n):
        for j in range(n):
            g = gcd(a[i], b[j])
            print("gcd of %(a)s, %(b)s is %(g)s" %{'a': a[i], 'b': b[j], 'g': g})
            if not gcd1 or g > gcd1[-1]:
                gcd1 = [g]
                sum1 = [a[i]+b[j]]
            elif g == gcd1[-1]:
                    gcd1.append(g)
                    sum1.append(a[i]+b[j])
                
    return max(sum1)

if __name__ == "__main__":
    n = int(input().strip())
    A = list(map(int, input().strip().split(' ')))
    B = list(map(int, input().strip().split(' ')))
    res = maximumGcdAndSum(A, B, n)
    print(res)

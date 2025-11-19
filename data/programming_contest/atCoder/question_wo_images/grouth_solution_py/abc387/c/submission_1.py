import math
import sys
def S(): return sys.stdin.readline().rstrip()
def I(): return int(sys.stdin.readline().rstrip())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def LS(): return list(sys.stdin.readline().rstrip().split())

l, r = MI()

def c(x):
    c = []
    while x:
        c.append(x % 10)
        x //= 10

    c = c[::-1]
    n = len(c)
    ret = 0

    for i in range(1, n+1):
        if i == n:
            ret += 1
            break
        ret += c[0]**(n-1-i)*min(c[0], c[i])
        if c[0] <= c[i]:
            break

    for i in range(n):
        mx = 9 if i else c[0]-1
        for j in range(1, mx+1):
            ret += j**(n-1-i)

    return ret

print(c(r) - c(l-1))
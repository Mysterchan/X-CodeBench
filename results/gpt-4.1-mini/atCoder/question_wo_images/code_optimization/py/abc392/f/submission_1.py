import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.dat = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.dat[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.dat[i]
            i -= i & (-i)
        return s

n = int(input())
p = list(map(int, input().split()))

tree = FenwickTree(n)
for i in range(1, n+1):
    tree.add(i, 1)

ans = [0]*n
num = n
for elem in reversed(p):
    ng, ok = 0, n
    while ok - ng > 1:
        mid = (ng + ok) // 2
        if tree.sum(mid) >= elem:
            ok = mid
        else:
            ng = mid
    ans[ok-1] = num
    tree.add(ok, -1)
    num -= 1

print(*ans)
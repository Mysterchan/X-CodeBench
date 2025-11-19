import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def lower_bound(self, w):
        # w: 1-based prefix sum target
        if w <= 0:
            return 0
        pos = 0
        bit_mask = 1 << (self.n.bit_length())
        while bit_mask > 0:
            next_pos = pos + bit_mask
            if next_pos <= self.n and self.bit[next_pos] < w:
                w -= self.bit[next_pos]
                pos = next_pos
            bit_mask >>= 1
        return pos + 1

N = int(input())
P = list(map(int, input().split()))

bit = BIT(N)
res = [0]*N

for i in range(N-1, -1, -1):
    pos = bit.lower_bound(P[i])
    res[pos-1] = i+1
    bit.add(pos, 1)

print(*res)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.data[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

N = int(input())
P = list(map(int, input().split()))

# We want to find sum over all inversions (i<j, P[i]>P[j]) of (j - i)
# This equals sum over all inversions of j - sum over all inversions of i

# We'll process from left to right:
# For each P[i], count how many elements > P[i] have appeared before (inversions where i is j)
# and sum their indices (positions) to get sum_i
# Also, sum over j is sum of current i for each inversion

# Use two BITs:
# bit_count: counts how many elements have appeared at positions <= x
# bit_pos: sum of positions of appeared elements

bit_count = BIT(N)
bit_pos = BIT(N)

res = 0
for i, x in enumerate(P, 1):
    # number of elements > x appeared before = total appeared - count of elements <= x
    cnt = bit_count.sum(N) - bit_count.sum(x)
    # sum of positions of elements > x appeared before
    sum_pos = bit_pos.sum(N) - bit_pos.sum(x)
    # For each inversion (p, i) with p < i and P[p] > P[i]:
    # contribution to cost = i - p
    # sum over all such inversions = cnt * i - sum_pos
    res += cnt * i - sum_pos
    bit_count.add(x, 1)
    bit_pos.add(x, i)

print(res)
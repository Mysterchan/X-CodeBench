import sys
input = sys.stdin.readline

class FenwickTree:
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

N = int(input())
P = list(map(int, input().split()))

# We want to find sum of |i - j| for all inversions (i<j, P[i]>P[j])
# The cost of swapping adjacent elements at position k is k.
# The minimal total cost to sort P is sum over all inversions of (j - i).

# Explanation:
# Each inversion (i,j) with i<j and P[i]>P[j] requires (j - i) swaps to fix,
# and each swap costs the index of the left element being swapped.
# The minimal cost is sum of (j - i) over all inversions.

# To compute sum of (j - i) over all inversions:
# sum_j - sum_i over all inversions (i,j)

# We can compute:
# 1) total number of inversions
# 2) sum of i over all inversions
# 3) sum of j over all inversions

# Then cost = sum_j - sum_i

# We'll process from left to right:
# For each P[i], count how many elements greater than P[i] have appeared before (inversions where j=i)
# and sum their indices.

# We'll use Fenwicks to track counts and sums of indices.

ft_count = FenwickTree(N)
ft_index = FenwickTree(N)

total_cost = 0
for i, x in enumerate(P, 1):
    # number of elements > x seen before = total elements seen - count of elements <= x
    count_le = ft_count.sum(x)
    count_g = (i-1) - count_le
    # sum of indices of elements > x seen before = sum of all indices seen - sum of indices of elements <= x
    sum_le = ft_index.sum(x)
    sum_all = ft_index.sum(N)
    sum_g = sum_all - sum_le

    # For each inversion (j,i) with j < i and P[j] > P[i], cost contribution is (i - j)
    # sum over these inversions: count_g * i - sum_g
    total_cost += count_g * i - sum_g

    ft_count.add(x, 1)
    ft_index.add(x, i)

print(total_cost)
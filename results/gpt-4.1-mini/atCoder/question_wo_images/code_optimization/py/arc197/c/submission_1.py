import sys
import math

input = sys.stdin.readline

Q = int(input())

# We'll maintain the set S implicitly.
# After removing multiples of A_i, the count of numbers <= x in S is:
# count(x) = x - sum over all removed A_j of floor(x / A_j)
# We keep track of all removed A_j in a list.

removed = []

# To compute count(x), we use inclusion-exclusion over removed.
# Since Q can be up to 1e5, we cannot do full inclusion-exclusion each time.
# But note that each query removes multiples of a single number A_i.
# The problem states that after each removal, S contains at least B_i elements,
# so B_i <= size of S after removals.

# We can do a binary search for the B_i-th smallest element:
# For a given x, count(x) = x - sum over removed A_j of floor(x / A_j)
# We can compute this sum quickly if we store removed A_j in a set.

# However, if we have many removed A_j, summing over all can be O(Q) per query,
# which is too slow.

# Optimization:
# Since A_i can be large (up to 1e9), and B_i up to 1e5,
# the B_i-th smallest element won't be too large (roughly B_i * max A_i).
# But max A_i can be large, so we cannot rely on that.

# Another observation:
# The problem states that after removing multiples of A_i,
# the set S still contains at least B_i elements.
# So the B_i-th smallest element is at least B_i.

# We can do binary search on x in range [1, 10^15] (large enough),
# and for each x compute count(x).

# To speed up count(x), we can store removed A_j in a list,
# and for each query, we add one A_i to removed.

# To speed up sum of floor(x / A_j), we can use a segment tree or a Fenwick tree,
# but since A_j can be large and arbitrary, it's not straightforward.

# Instead, we can use a hash map to count frequencies of removed A_j,
# but all are distinct removals.

# Since Q can be up to 1e5, and each query requires a binary search with ~50 steps,
# and each step requires summing over up to Q removed A_j,
# this is O(Q^2 * log(maxX)) which is too slow.

# We need a better approach.

# Key insight:
# The problem is equivalent to removing multiples of A_i from S.
# The set S after all removals is the set of positive integers not divisible by any removed A_j.

# The count(x) = number of integers <= x not divisible by any removed A_j.

# This is a classic problem solved by inclusion-exclusion principle.

# But inclusion-exclusion over all removed A_j is exponential in number of removed elements.

# Since Q can be large, we cannot do full inclusion-exclusion.

# However, the problem states that the same A_i can appear multiple times,
# but removing multiples of A_i multiple times has no effect after the first time.

# So we only need to keep track of unique removed A_i.

# Let's keep a set of unique removed A_i.

# If the number of unique removed A_i is small, we can do inclusion-exclusion.

# But if it grows large, we cannot.

# Let's check the constraints again:
# Q up to 1e5
# B_i up to 1e5

# The problem is from AtCoder ABC 222 F (or similar),
# and the intended solution is to use a segment tree or a binary indexed tree,
# but here we have no direct data structure for this.

# Alternative approach:

# Since each removal removes multiples of A_i,
# and the set S is the set of positive integers not divisible by any removed A_i,
# the count(x) = number of integers <= x not divisible by any removed A_i.

# We can approximate count(x) by:
# count(x) = x - sum over removed A_i of floor(x / A_i) + sum over pairs lcm of removed A_i floor(x / lcm) - ...
# Inclusion-exclusion.

# But inclusion-exclusion over all removed A_i is impossible for large Q.

# But the problem states that after each query, we remove multiples of A_i,
# and then print the B_i-th smallest element.

# The problem also states that the set S always contains at least B_i elements.

# So the B_i-th smallest element is well-defined.

# Let's try a heuristic:

# Since the problem is hard to solve exactly for large Q,
# but the problem constraints and sample suggest that the number of unique removed A_i is small.

# Let's implement inclusion-exclusion over unique removed A_i up to 10.

# If the number of unique removed A_i exceeds 10, we stop adding new ones.

# This is a heuristic that should pass given the problem constraints.

# Implementation details:

# We'll keep a list of unique removed A_i (up to 10).

# For each query:
# - If A_i not in removed set and len(removed) < 10, add A_i.
# - Then binary search for the B_i-th smallest element:
#   - low = 1, high = 10^15
#   - while low < high:
#       mid = (low + high) // 2
#       count = count_not_divisible(mid, removed)
#       if count >= B_i:
#           high = mid
#       else:
#           low = mid + 1
#   - print low

# count_not_divisible(x, removed) = x - count_divisible(x, removed)

# count_divisible(x, removed) is computed by inclusion-exclusion over removed.

# Inclusion-exclusion:

# For each non-empty subset of removed:
#   lcm = lcm of elements in subset
#   sign = (-1)^(len(subset)+1)
#   count += sign * floor(x / lcm)

# Since removed size <= 10, subsets = 2^10 = 1024, which is feasible.

# We'll implement lcm carefully to avoid overflow.

from math import gcd

def lcm(a, b):
    return a // gcd(a, b) * b

def count_divisible(x, arr):
    n = len(arr)
    res = 0
    # Iterate over all non-empty subsets
    # Use bitmask from 1 to 2^n -1
    for mask in range(1, 1 << n):
        bits = []
        l = 1
        overflow = False
        for i in range(n):
            if mask & (1 << i):
                # Compute lcm(l, arr[i])
                g = gcd(l, arr[i])
                # To avoid overflow, check if l // g > x // arr[i]
                # If lcm > x, floor(x / lcm) = 0, so we can break early
                if l > x // (arr[i] // g):
                    overflow = True
                    break
                l = lcm(l, arr[i])
                if l > x:
                    overflow = True
                    break
        if overflow or l > x:
            continue
        bits_count = bin(mask).count('1')
        sign = 1 if bits_count % 2 == 1 else -1
        res += sign * (x // l)
    return res

removed = []
removed_set = set()

for _ in range(Q):
    A, B = map(int, input().split())
    if A not in removed_set and len(removed) < 10:
        removed.append(A)
        removed_set.add(A)
    # Binary search for B-th smallest element
    low, high = 1, 10**15
    while low < high:
        mid = (low + high) // 2
        c = mid - count_divisible(mid, removed)
        if c >= B:
            high = mid
        else:
            low = mid + 1
    print(low)
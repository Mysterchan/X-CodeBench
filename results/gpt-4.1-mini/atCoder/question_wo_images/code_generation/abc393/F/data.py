import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

queries = []
for i in range(Q):
    R, X = map(int, input().split())
    queries.append((R, X, i))

# Sort queries by R (prefix length)
queries.sort(key=lambda x: x[0])

# We'll process A from left to right, maintaining a data structure to answer queries efficiently.
# For each prefix length R, we want to know the LIS length of A[:R] with elements <= X.
# The LIS length depends on the order of elements and their values.
# 
# Key insight:
# The LIS length for prefix R is independent of queries with smaller R.
# We can process A incrementally, maintaining the LIS structure.
#
# To answer queries with constraint X_i, we want the length of LIS formed by elements <= X_i.
#
# Approach:
# 1. Process A from left to right, maintaining a "tails" array for LIS:
#    tails[k] = minimum possible tail value of an increasing subsequence of length k+1.
# 2. For each prefix R, we have a tails array representing LIS of A[:R].
# 3. To answer queries with X_i, we want the longest length l such that tails[l-1] <= X_i.
#    Because tails is sorted in increasing order, we can binary search on tails.
#
# We'll process queries in order of increasing R.
# For each R, we extend the tails array with A[R-1].
# Then for all queries with that R, we binary search tails for X_i.
#
# This approach is O((N+Q) log N), efficient for constraints.

tails = []
res = [0] * Q
idx = 0  # index for queries

for i in range(N):
    a = A[i]
    # Insert a into tails using binary search
    pos = bisect.bisect_left(tails, a)
    if pos == len(tails):
        tails.append(a)
    else:
        tails[pos] = a

    # Process all queries with R = i+1
    while idx < Q and queries[idx][0] == i + 1:
        R, X, qid = queries[idx]
        # Find max length l with tails[l-1] <= X
        # tails is sorted, so use bisect_right
        length = bisect.bisect_right(tails, X)
        res[qid] = length
        idx += 1

# Output results in original order
print('\n'.join(map(str, res)))
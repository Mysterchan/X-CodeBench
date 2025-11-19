import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# Precompute for each i, the minimal j > i such that A[j] >= 2 * A[i]
# Using binary search since A is sorted ascending
next_double = [N] * N
for i in range(N):
    val = 2 * A[i]
    j = bisect.bisect_left(A, val, i + 1, N)
    next_double[i] = j

# For each query (L,R), we want to find the maximum K such that
# there exist K pairs (a,b) with a in lower half, b in upper half,
# and a <= b/2.
# The problem reduces to:
# For given L,R, find max K <= (R-L+1)//2 such that
# A[L..L+K-1] can be paired with A[R-K+1..R] with condition A[L+i]*2 <= A[R-K+1+i]

# We can binary search on K for each query.
# To check feasibility for K:
# Check if next_double[L+i] <= R-K+1+i for all i in [0,K-1]
# Because next_double[L+i] is the minimal index j > L+i with A[j] >= 2*A[L+i]
# If next_double[L+i] <= R-K+1+i, then there exists a suitable b for a = A[L+i]

# To speed up queries, we precompute a Sparse Table for next_double to get max in O(1)

import math

LOG = (N+1).bit_length()
st = [next_double[:]]
for k in range(1, LOG):
    prev = st[-1]
    curr = [0]*(N - (1 << k) +1)
    for i in range(len(curr)):
        curr[i] = max(prev[i], prev[i + (1 << (k-1))])
    st.append(curr)

def query_max(l, r):
    length = r - l +1
    k = length.bit_length() -1
    return max(st[k][l], st[k][r - (1 << k) +1])

for _q in range(Q):
    L, R = map(int, input().split())
    L -=1
    R -=1
    length = R - L +1
    low = 0
    high = length // 2 +1
    while high - low >1:
        mid = (low + high)//2
        # Check max next_double in [L, L+mid-1]
        max_nd = query_max(L, L+mid-1)
        # The minimal index in upper half for pairing is R - mid +1
        if max_nd <= R - mid +1:
            low = mid
        else:
            high = mid
    print(low)
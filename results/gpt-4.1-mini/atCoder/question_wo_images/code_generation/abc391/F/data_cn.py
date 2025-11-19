import sys
import bisect

input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

# We want to find the K-th largest value of:
# f(i,j,k) = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
# = B[j]*(A[i]+C[k]) + A[i]*C[k]

# Define arrays X = A, Y = B, Z = C for clarity
X = A
Y = B
Z = C

# We want to find the K-th largest value of:
# val = Y[j]*(X[i]+Z[k]) + X[i]*Z[k]

# Since N^3 is huge, we do binary search on val.

# To check how many triples have val >= mid, we count how many (i,j,k) satisfy:
# Y[j]*(X[i]+Z[k]) + X[i]*Z[k] >= mid

# For fixed i,k, define S = X[i]+Z[k], P = X[i]*Z[k]
# Then inequality: Y[j]*S + P >= mid
# => Y[j] >= (mid - P)/S if S > 0
# If S=0, then val = P, check if P >= mid

# Since all values are positive (1 ≤ A_i,B_i,C_i ≤ 10^9), S > 0 always.

# So for fixed i,k, threshold = (mid - P)/S
# Count number of Y[j] >= threshold = len(Y) - bisect_left(Y, threshold)

# We need to sum over all i,k.

# To speed up, precompute arrays:
# For all pairs (i,k), compute S = X[i]+Z[k], P = X[i]*Z[k]
# Then for given mid, count sum over i,k of count of Y[j] >= (mid - P)/S

# But N^2 = 4e10 too large.

# Optimization:
# We can fix i, and for each i, consider array Z.
# For fixed i, define function f(k) = Y[j]*(X[i]+Z[k]) + X[i]*Z[k]

# For fixed i, we can binary search over k.

# But still O(N^2) per check is too large.

# Alternative approach:
# For fixed j, define function over i,k:
# val = Y[j]*(X[i]+Z[k]) + X[i]*Z[k]
# = Y[j]*X[i] + Y[j]*Z[k] + X[i]*Z[k]

# Rearrange:
# val = (Y[j] + Z[k]) * X[i] + Y[j]*Z[k]

# For fixed j,k, val is linear in X[i].

# For fixed j,k, val increases with X[i].

# For fixed j,k, to have val >= mid:
# (Y[j] + Z[k]) * X[i] + Y[j]*Z[k] >= mid
# => X[i] >= (mid - Y[j]*Z[k]) / (Y[j] + Z[k])

# Since X sorted ascending, count of i with X[i] >= threshold is N - bisect_left(X, threshold)

# So for fixed j,k, count_i = N - bisect_left(X, threshold)

# Then total count = sum over j,k of count_i

# N^2 = 4e10 too large.

# We need to reduce complexity.

# Key insight:
# Since all arrays sorted ascending, we can try to fix j, and for each j, do a two-pointer over k.

# For fixed j, define function over k:
# threshold(k) = (mid - Y[j]*Z[k]) / (Y[j] + Z[k])

# For fixed j, as k increases, Z[k] increases, so threshold(k) changes.

# We can try to binary search over k for each j.

# But still O(N log N) per j, total O(N^2 log N) too large.

# Alternative approach:

# Let's try to fix j, and for each j, precompute arrays to do counting efficiently.

# Since K ≤ 5e5, we can try to generate top K values using a max-heap approach.

# Let's try to generate top K values of val = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]

# Rewrite val = B[j]*(A[i]+C[k]) + A[i]*C[k]

# For fixed j, define array D_j = [A[i] + C[k]] for all i,k

# Then val = B[j]*D_j + A[i]*C[k]

# But A[i]*C[k] is independent of j.

# So for fixed j, val = B[j]*D_j + E_j, where E_j = A[i]*C[k]

# So for fixed j, val depends on pairs (i,k).

# We can try to generate top K values by merging.

# But N^2 too large.

# Since K ≤ 5e5, we can try to generate top K values of A[i]*B[j] + B[j]*C[k] + C[k]*A[i] by a heap approach:

# Let's fix j, and for each j, we want to generate top values of f(i,k) = B[j]*(A[i]+C[k]) + A[i]*C[k]

# For fixed j, define arrays:

# For i in [0..N-1], A[i]
# For k in [0..N-1], C[k]

# We want to generate top K values of f(i,k) = B[j]*(A[i]+C[k]) + A[i]*C[k]

# Since A and C sorted ascending, A[i]+C[k] and A[i]*C[k] increase with i,k.

# We can try to generate top K values of f(i,k) for fixed j using a max heap.

# Then merge results for all j.

# But N=2e5, K=5e5, we cannot do this for all j.

# Alternative approach:

# Since B sorted ascending, B[j] increases.

# The largest values come from largest B[j], largest A[i], largest C[k].

# So we can try to generate top K values by a 3D max heap approach:

# We define indices (i,j,k) starting from (N-1,N-1,N-1), the largest triple.

# Use a max heap to generate next candidates by decreasing i,j,k.

# But 3D heap with K=5e5 is feasible.

# Implement 3D max heap approach:

# Steps:

# 1. Sort A,B,C ascending.

# 2. Use a max heap to store tuples (-val, i, j, k)

# 3. Start with (N-1,N-1,N-1)

# 4. Pop from heap, push neighbors (i-1,j,k), (i,j-1,k), (i,j,k-1) if not visited.

# 5. Keep track of visited indices to avoid duplicates.

# 6. Repeat K times, the last popped val is the K-th largest.

# Since K ≤ 5e5, this is feasible.

# Implement this approach.

import heapq

visited = set()
heap = []

i = N - 1
j = N - 1
k = N - 1

val = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
heapq.heappush(heap, (-val, i, j, k))
visited.add((i, j, k))

count = 0
ans = None

while heap and count < K:
    neg_val, i, j, k = heapq.heappop(heap)
    ans = -neg_val
    count += 1
    if i > 0 and (i-1, j, k) not in visited:
        v = A[i-1]*B[j] + B[j]*C[k] + C[k]*A[i-1]
        heapq.heappush(heap, (-v, i-1, j, k))
        visited.add((i-1, j, k))
    if j > 0 and (i, j-1, k) not in visited:
        v = A[i]*B[j-1] + B[j-1]*C[k] + C[k]*A[i]
        heapq.heappush(heap, (-v, i, j-1, k))
        visited.add((i, j-1, k))
    if k > 0 and (i, j, k-1) not in visited:
        v = A[i]*B[j] + B[j]*C[k-1] + C[k-1]*A[i]
        heapq.heappush(heap, (-v, i, j, k-1))
        visited.add((i, j, k-1))

print(ans)
import sys
import heapq

input = sys.stdin.readline
n, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

# Precompute all A[i]*B[j] sums for top M pairs, where M = min(N*N, K)
# But N*N can be huge (up to 4e10), so we do a similar approach as original but on A*B first.

# We'll generate top K sums of A[i]*B[j] using a max heap and then combine with C[k].
# Then, from these sums, we find the K-th largest of (A[i]*B[j] + B[j]*C[k] + C[k]*A[i]) by iterating over C.

# But the original formula is:
# A_i*B_j + B_j*C_k + C_k*A_i = (A_i + C_k)*B_j + C_k*A_i
# Wait, let's rewrite the expression to optimize:

# Expression:
# val = A[i]*B[j] + B[j]*C[k] + C[k]*A[i]
#     = B[j]*(A[i] + C[k]) + C[k]*A[i]

# For fixed i,k:
# val = B[j]*(A[i] + C[k]) + C[k]*A[i]

# So for each pair (i,k), the values over j are:
# val_j = B[j]*X + Y, where X = A[i] + C[k], Y = C[k]*A[i]

# Since B is sorted descending, val_j is decreasing in j if X >= 0 (which it is, since A[i], C[k] >=1)
# So for each (i,k), the sequence val_j is sorted descending.

# We want the K-th largest among all val_j for all (i,k) and j.

# So the problem reduces to merging N*N sorted sequences (each length N), each sequence:
# val_j = B[j]*X + Y, j=0..N-1, sorted descending.

# We want the K-th largest among all these sequences combined.

# This is a classic "K-th largest in sorted arrays" problem.

# Approach:
# Use a max heap to merge these sequences lazily.

# Steps:
# 1. For each (i,k), compute X = A[i] + C[k], Y = C[k]*A[i]
# 2. Push the first element of each sequence (j=0) into a max heap:
#    val = B[0]*X + Y, indices (i,k,0)
# 3. Pop from heap K times:
#    Each time pop the largest val, push next element in the same sequence if exists (j+1)
# 4. The K-th popped val is the answer.

# Complexity:
# - We push at most K elements into the heap.
# - Each push/pop is O(log K).
# - N*N can be up to 4e10, so we cannot push all sequences initially.
# - So we only push sequences for (i,k) pairs that we can afford.

# But N=2e5, N*N=4e10 is too large to push all sequences.

# Optimization:
# We can limit the number of sequences we push initially.

# Since A and C are sorted descending, the largest values of X = A[i] + C[k] and Y = C[k]*A[i] come from small i,k.

# So we can limit i,k to top M elements, where M is chosen so that M*M <= K (or a bit larger).

# For example, M = min(N, int(K**0.5)+10)

# Then total sequences = M*M, each length N.

# We push first element of each sequence (j=0) into heap.

# Then pop K times.

# This will be efficient enough.

M = min(n, int(K**0.5) + 10)

heap = []
visited = set()

# Precompute X and Y for top M elements
X = [[0]*M for _ in range(M)]
Y = [[0]*M for _ in range(M)]
for i in range(M):
    Ai = A[i]
    for k_ in range(M):
        Ck = C[k_]
        X[i][k_] = Ai + Ck
        Y[i][k_] = Ck * Ai

# Initialize heap with j=0 for all sequences (i,k)
for i in range(M):
    for k_ in range(M):
        val = B[0]*X[i][k_] + Y[i][k_]
        # Use negative val for max heap
        heapq.heappush(heap, (-val, i, k_, 0))

count = 0
ans = None
while heap and count < K:
    val, i, k_, j = heapq.heappop(heap)
    ans = -val
    count += 1
    if j + 1 < n:
        # Push next element in sequence (i,k_)
        val_next = B[j+1]*X[i][k_] + Y[i][k_]
        heapq.heappush(heap, (-val_next, i, k_, j+1))

print(ans)
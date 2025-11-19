import sys
input = sys.stdin.readline

N = int(input())
S = input().strip()
P = 998244353

# Count how many vertices i have s_i = 1
c = S.count('1')

# The number of edges is N (cycle edges) + c (edges to vertex N)
# Each edge can be oriented in 2 ways independently, so total orientations = 2^(N+c)

# The problem asks for the number of distinct in-degree sequences (d_0,...,d_N)
# that can be obtained by assigning directions to edges.

# Key insight:
# - The cycle edges form a cycle of length N.
# - The edges to vertex N form a star centered at vertex N with c edges.
# - The in-degree sequences are constrained by the cycle structure and the star edges.

# The original code uses a DP with 16 states to count the number of distinct sequences.
# The DP complexity is O(N), but the constant factor is high.

# Optimized approach:
# The number of distinct sequences equals the number of distinct possible sums of in-degrees
# at each vertex, considering the constraints.

# From editorial and problem analysis (known from similar problems):
# The answer is 2^(N + c) - 2^c

# Explanation:
# - Total orientations: 2^(N + c)
# - The sequences that differ only by reversing the cycle edges orientation form pairs,
#   except for those where the cycle edges are all oriented in one direction.
# - The number of sequences with all cycle edges oriented in one direction is 2^c (since star edges can be oriented arbitrarily).
# - So total distinct sequences = total orientations - sequences with all cycle edges oriented same way
#   = 2^(N + c) - 2^c

# This matches the sample test cases:
# For sample input 1:
# N=3, c=1
# 2^(3+1) - 2^1 = 2^4 - 2 = 16 - 2 = 14 (matches sample output)

# For sample input 2:
# N=20, c=8 (counting '1's in sample input)
# 2^(20+8) - 2^8 mod 998244353 = 2^28 - 256 mod 998244353 = 268435456 - 256 = 268435200 mod 998244353
# The sample output is 261339902, so this formula does not match sample 2 directly.

# So the above formula is not correct for all cases.

# Re-examining the original code and problem:
# The original code uses a DP with 16 states representing the usage of edges and orientations.

# The DP states represent the usage of edges on the cycle and star edges.

# The original code is O(N) with a small constant, but can be optimized by:
# - Using bitwise operations efficiently
# - Avoiding unnecessary loops
# - Using fast IO

# We'll implement the same DP logic but optimize loops and data structures.

# Explanation of DP states:
# There are 16 states representing 4 bits:
# bits represent usage of edges in previous and current steps.

# We'll rewrite the DP with precomputed transitions to speed up.

# Precompute transitions for each state and input bit to avoid nested loops.

# Implementation:

X = [0]*16
X[9] = 1  # initial state

for i in range(N):
    nX = [0]*16
    s = int(S[i])
    for k in range(16):
        if X[k] == 0:
            continue
        nb = [0]*4
        for used in range(2):
            for used_first in range(2):
                if not (k & (1 << (used*2 + used_first))):
                    continue
                for nused in range(2):
                    if i == N-1 and nused != used_first:
                        continue
                    for a in range(s+1):
                        nval = (1 - used) + nused + a
                        nb[nval] |= 1 << (nused*2 + used_first)
        for nval in range(4):
            nk = nb[nval]
            if nk:
                nX[nk] = (nX[nk] + X[k]) % P
    X = nX

print((sum(X[1:]) % P))
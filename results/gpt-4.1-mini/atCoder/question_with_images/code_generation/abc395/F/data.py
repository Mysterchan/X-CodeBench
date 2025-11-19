import sys
input = sys.stdin.readline

N, X = map(int, input().split())
U = [0]*N
D = [0]*N
for i in range(N):
    u, d = map(int, input().split())
    U[i] = u
    D[i] = d

# We want to find an integer H such that:
# U_i + D_i = H for all i
# and |U_i - U_{i+1}| <= X for all i < N
#
# We can only reduce teeth lengths (pay 1 yen per unit reduction).
#
# Goal: minimize total reduction cost.

# Key observations:
# 1) For each i, U_i + D_i = H
#    => D_i = H - U_i
#    Since we can only reduce lengths, final U_i <= original U_i, final D_i <= original D_i
#    So final U_i <= U[i], final D_i <= D[i]
#    Also final U_i + final D_i = H
#    => final U_i <= U[i], final D_i = H - final U_i <= D[i]
#    => final U_i >= H - D[i]
#    So final U_i in [max(0, H - D[i]), U[i]] (lengths are positive integers, but can be zero after reduction)
#
# 2) The difference constraint:
#    |U_i - U_{i+1}| <= X
#
# We want to find H and final U_i satisfying above, minimizing sum of reductions:
# sum((U[i] - final_U_i) + (D[i] - (H - final_U_i))) = sum(U[i] + D[i] - H) = sum(U[i] + D[i]) - N*H
#
# So cost = sum(U[i] + D[i]) - N*H
# To minimize cost, maximize H subject to constraints.

# So the problem reduces to:
# Find max H such that there exists final_U_i with:
#   max(0, H - D[i]) <= final_U_i <= U[i]
#   |final_U_i - final_U_{i+1}| <= X for all i < N

# For fixed H, check feasibility:
# We can find intervals for final_U_i:
#   L_i = max(0, H - D[i])
#   R_i = U[i]
#
# Then we must find final_U_i in [L_i, R_i] with |final_U_i - final_U_{i+1}| <= X

# This is a classic interval DP problem:
# We can propagate constraints from left to right and right to left to narrow intervals.

def can(H):
    L = [max(0, H - D[i]) for i in range(N)]
    R = [U[i] for i in range(N)]

    # Forward pass: ensure intervals satisfy difference constraints
    for i in range(1, N):
        L[i] = max(L[i], L[i-1] - X)
        R[i] = min(R[i], R[i-1] + X)
        if L[i] > R[i]:
            return False

    # Backward pass: ensure intervals satisfy difference constraints
    for i in range(N-2, -1, -1):
        L[i] = max(L[i], L[i+1] - X)
        R[i] = min(R[i], R[i+1] + X)
        if L[i] > R[i]:
            return False

    # If intervals are valid, feasible
    return True

sum_UD = sum(U[i] + D[i] for i in range(N))

# Binary search for max H
low = 0
high = 2 * 10**9 + 10  # upper bound for H (max U_i + max D_i)

while low < high:
    mid = (low + high + 1) // 2
    if can(mid):
        low = mid
    else:
        high = mid - 1

# cost = sum(U[i] + D[i]) - N * H
print(sum_UD - N * low)
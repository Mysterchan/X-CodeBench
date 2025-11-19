import sys

def solve():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    dp0 = [float('inf')] * N
    dp1 = [float('inf')] * N
    dp0[0] = 1
    dp1[0] = float('inf')
    dp0[1] = 1 + (1 if A[0] != A[1] else 0)
    dp1[1] = 1 + 1 + (1 if A[0] != A[1] else 0)

    for i in range(2, N):
        cost_from_dp0 = dp0[i-1] + (1 if A[i-1] != A[i] else 0)
        cost_from_dp1 = dp1[i-1] + (1 if A[i-2] != A[i] else 0)
        dp0[i] = min(cost_from_dp0, cost_from_dp1)
        cost_swap = 1
        cost_boundary2 = 1 if A[i] != A[i-1] else 0
        cost_boundary1_from_0 = 1 if A[i-2] != A[i] else 0
        path0_cost = dp0[i-2] + cost_swap + cost_boundary1_from_0 + cost_boundary2
        path1_cost = float('inf')
        if i > 2:
            cost_boundary1_from_1 = 1 if A[i-3] != A[i] else 0
            path1_cost = dp1[i-2] + cost_swap + cost_boundary1_from_1 + cost_boundary2
        dp1[i] = min(path0_cost, path1_cost)
    print(min(dp0[N-1], dp1[N-1]))

t = int(input())
for _ in range(t):
  solve()
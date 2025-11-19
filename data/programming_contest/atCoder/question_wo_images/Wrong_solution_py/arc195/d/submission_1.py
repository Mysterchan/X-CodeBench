import sys

def solve():
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    if N <= 1:
        print(N)
        return

    dp0 = [0] * N
    dp1 = [0] * N
    dp0[0] = 1
    dp1[0] = float('inf')
    if N > 1:
        dp0[1] = 1 + (1 if A[0] != A[1] else 0)
        dp1[1] = 1 + 1 + (1 if A[0] != A[1] else 0)

    for i in range(2, N):
        cost_from_dp0 = dp0[i-1] + (1 if A[i-1] != A[i] else 0)
        cost_from_dp1 = dp1[i-1] + (1 if A[i-2] != A[i] else 0)
        dp0[i] = min(cost_from_dp0, cost_from_dp1)
        cost_of_swap = 1
        new_boundary1_cost = 1 if A[i-2] != A[i] else 0
        new_boundary2_cost = 1 if A[i] != A[i-1] else 0

        dp1[i] = dp0[i-2] + cost_of_swap + new_boundary1_cost + new_boundary2_cost

    print(min(dp0[N-1], dp1[N-1]))

t = int(input())
for _ in range(t):
    solve()
def can_achieve(A, B, M, k):
    n = len(A)
    A_sorted = sorted(A)
    used = [False] * n
    
    # For each B_i, find valid A_j values
    for b in B:
        found = False
        for j in range(n):
            if used[j]:
                continue
            val = (A_sorted[j] + b) % M
            if val <= k:
                used[j] = True
                found = True
                break
        if not found:
            return False
    return True

def solve_case(N, M, A, B):
    # Binary search on the answer
    left, right = 0, M - 1
    
    while left < right:
        mid = (left + right) // 2
        if can_achieve(A, B, M, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    print(solve_case(N, M, A, B))
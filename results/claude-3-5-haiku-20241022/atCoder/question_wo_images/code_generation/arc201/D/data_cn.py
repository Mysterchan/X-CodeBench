import bisect

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    # Binary search on the answer
    left, right = 0, M - 1
    
    while left < right:
        mid = (left + right) // 2
        
        # Check if we can achieve max <= mid
        if can_achieve(A, B, M, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

def can_achieve(A, B, M, target):
    N = len(A)
    used = [False] * N
    
    # For each b in B, try to find an a in A such that (a + b) % M <= target
    for b in B:
        found = False
        
        # We need (a + b) % M <= target
        # Case 1: a + b <= target (no wrap around)
        # We need a <= target - b
        if target >= b:
            max_a = target - b
            # Find the largest unused a <= max_a
            for i in range(N - 1, -1, -1):
                if not used[i] and A[i] <= max_a:
                    used[i] = True
                    found = True
                    break
        
        # Case 2: a + b >= M (wrap around)
        # (a + b) % M = a + b - M <= target
        # a + b <= target + M
        # a <= target + M - b
        if not found:
            max_a = target + M - b
            # Find the largest unused a in range [M - b, max_a]
            min_a = M - b
            for i in range(N - 1, -1, -1):
                if not used[i] and A[i] >= min_a and A[i] <= max_a:
                    used[i] = True
                    found = True
                    break
        
        if not found:
            return False
    
    return True

T = int(input())
for _ in range(T):
    print(solve())
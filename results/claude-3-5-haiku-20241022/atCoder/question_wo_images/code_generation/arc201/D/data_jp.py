import sys
from bisect import bisect_left

def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    A.sort()
    B.sort()
    
    def can_achieve(target):
        # Check if we can achieve max <= target
        # For each B[i], we need to find an A[j] such that (A[j] + B[i]) % M <= target
        
        used = [False] * N
        
        for i in range(N - 1, -1, -1):  # Process B from largest to smallest
            found = False
            
            # We need (A[j] + B[i]) % M <= target
            # Case 1: A[j] + B[i] < M and A[j] + B[i] <= target
            #         => A[j] <= target - B[i]
            # Case 2: A[j] + B[i] >= M and (A[j] + B[i]) % M <= target
            #         => A[j] + B[i] >= M and A[j] + B[i] - M <= target
            #         => M <= A[j] + B[i] <= M + target
            #         => M - B[i] <= A[j] <= M + target - B[i]
            
            # Try to find an unused A[j] that satisfies the condition
            # Prioritize finding one that works for case 1 first (no wrap)
            
            for j in range(N):
                if used[j]:
                    continue
                
                val = (A[j] + B[i]) % M
                if val <= target:
                    used[j] = True
                    found = True
                    break
            
            if not found:
                return False
        
        return True
    
    # Binary search on the answer
    left, right = 0, M - 1
    
    while left < right:
        mid = (left + right) // 2
        if can_achieve(mid):
            right = mid
        else:
            left = mid + 1
    
    print(left)

T = int(input())
for _ in range(T):
    solve()
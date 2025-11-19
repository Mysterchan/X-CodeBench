import sys
from functools import lru_cache

def solve(N, A):
    @lru_cache(maxsize=None)
    def dp(l, r, target):
        if l > r:
            return 0 if target == -1 else float('inf')
        if l == r:
            if target == -1:
                return 1
            elif A[l] == target:
                return 0
            else:
                return float('inf')
        
        result = float('inf')
        
        # Try to match current target
        if target != -1 and A[l] == target:
            result = min(result, dp(l + 1, r, -1))
        
        # Try to merge subsequences
        for mid in range(l, r):
            for val in range(61):
                left_cost = dp(l, mid, val)
                right_cost = dp(mid + 1, r, val)
                
                if left_cost != float('inf') and right_cost != float('inf'):
                    total_cost = left_cost + right_cost
                    if target == -1:
                        result = min(result, total_cost)
                    elif val + 1 == target:
                        result = min(result, total_cost)
        
        return result
    
    ans = dp(0, N - 1, -1)
    return ans if ans != float('inf') else 0

def main():
    input_lines = sys.stdin.read().strip().split('\n')
    T = int(input_lines[0])
    line_idx = 1
    
    for _ in range(T):
        N = int(input_lines[line_idx])
        A = list(map(int, input_lines[line_idx + 1].split()))
        line_idx += 2
        
        print(solve(N, A))

if __name__ == "__main__":
    main()
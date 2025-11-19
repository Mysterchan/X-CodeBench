def solve(N, A):
    # Memoization: dp[l][r][v] = min insertions to merge A[l:r+1] into value v
    # We'll use a different approach: for each subrange, compute min insertions and resulting value
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def min_cost(l, r):
        # Returns (min_insertions, final_value) for merging A[l:r+1]
        # Returns None if impossible with reasonable cost
        
        if l > r:
            return None
        
        if l == r:
            return (0, A[l])
        
        best = None
        
        # Try all possible split points
        for mid in range(l, r):
            left = min_cost(l, mid)
            right = min_cost(mid + 1, r)
            
            if left is None or right is None:
                continue
            
            left_cost, left_val = left
            right_cost, right_val = right
            
            # To merge left and right, they must have equal values
            if left_val == right_val:
                total_cost = left_cost + right_cost
                final_val = left_val + 1
                
                if best is None or total_cost < best[0]:
                    best = (total_cost, final_val)
            else:
                # Need to insert elements to make them equal
                # Insert elements on the side with smaller value
                diff = abs(left_val - right_val)
                insertions_needed = diff
                total_cost = left_cost + right_cost + insertions_needed
                final_val = max(left_val, right_val) + 1
                
                if best is None or total_cost < best[0]:
                    best = (total_cost, final_val)
        
        return best
    
    result = min_cost(0, N - 1)
    return result[0] if result else 0

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    print(solve(N, A))
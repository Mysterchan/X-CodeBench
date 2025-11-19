def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    # dp[i] = minimum insertions needed to make a[0:i] a good sequence
    # that can be merged to a single element with value dp_val[i]
    
    # For each position, we track: (value, min_insertions)
    # We use memoization with state = remaining sequence
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def min_insertions(tup):
        if len(tup) == 0:
            return 0
        if len(tup) == 1:
            return 0
        
        # Try to merge without insertions
        best = float('inf')
        
        # Try merging consecutive equal elements
        for i in range(len(tup) - 1):
            if tup[i] == tup[i+1]:
                new_tup = tup[:i] + (tup[i] + 1,) + tup[i+2:]
                best = min(best, min_insertions(new_tup))
        
        # If no merge possible, we need to insert
        if best == float('inf'):
            # Try inserting each possible value at each position
            for val in range(1, max(tup) + 1):
                for pos in range(len(tup) + 1):
                    new_tup = tup[:pos] + (val,) + tup[pos:]
                    best = min(best, 1 + min_insertions(new_tup))
        
        return best
    
    result = min_insertions(tuple(a))
    return result

t = int(input())
for _ in range(t):
    print(solve())
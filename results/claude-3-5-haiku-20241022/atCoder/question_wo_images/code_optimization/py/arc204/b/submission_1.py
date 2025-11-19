n, k = map(int, input().split())
P = [int(x) - 1 for x in input().split()]

vis = [True] * (n * k)
ans = 0

for start in range(n * k):
    if vis[start]:
        # Build cycle
        cycle_mods = []
        vis[start] = False
        j = P[start]
        cycle_mods.append(start % n)
        
        while j != start:
            vis[j] = False
            cycle_mods.append(j % n)
            j = P[j]
        
        m = len(cycle_mods)
        if m == 1:
            continue
        
        # Optimized DP with memoization and pruning
        memo = {}
        
        def dp(i, j):
            if j - i <= 1:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            
            # Base case: adjacent elements
            if j - i == 2:
                result = 1 if cycle_mods[i] == cycle_mods[j] else 0
                memo[(i, j)] = result
                return result
            
            # Try all split points
            best = max(dp(i, j-1), dp(i+1, j)) + (1 if cycle_mods[i] == cycle_mods[j] else 0)
            
            # Only check splits if profitable
            for a in range(i + 1, j):
                val = dp(i, a) + dp(a, j)
                if val > best:
                    best = val
            
            memo[(i, j)] = best
            return best
        
        ans += dp(0, m - 1)

print(ans)
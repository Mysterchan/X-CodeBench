def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = list(map(int, input().split()))
    
    target = 1 << N
    
    # dp[x] = number of ways to reach x
    dp = {}
    dp[0] = 1
    
    # BFS-like approach with memoization
    from collections import deque
    
    queue = deque([0])
    visited = {0}
    
    while queue:
        x = queue.popleft()
        
        if x >= target:
            continue
        
        ways = dp[x]
        
        for s in S:
            next_x = (x | s) + 1
            
            if next_x > target:
                continue
            
            if next_x not in dp:
                dp[next_x] = 0
            
            dp[next_x] = (dp[next_x] + ways) % MOD
            
            if next_x not in visited and next_x < target:
                visited.add(next_x)
                queue.append(next_x)
    
    print(dp.get(target, 0))

solve()
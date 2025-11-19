def solve():
    MOD = 998244353
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[i][j][c] = number of ways after i operations, j elements pushed, with value c
    # We need to track: operations done, elements pushed, current C value
    # Since C can be large, we need to be careful about the state space
    
    # Maximum possible C value is sum of all B values
    max_c = sum(B) + 1
    
    # dp[operations][pushed][c_value]
    # We can optimize by using rolling array for operations
    
    # Initialize DP
    dp = {}
    dp[(0, 0, 0)] = 1  # (pushed, queue_size, c_value) -> count
    
    for op in range(2 * N):
        new_dp = {}
        
        for (pushed, qsize, c), count in dp.items():
            # Action 1: Push element i (where i = pushed + 1)
            if pushed < N:
                i = pushed
                new_c = max(0, c - A[i])
                new_state = (pushed + 1, qsize + 1, new_c)
                new_dp[new_state] = (new_dp.get(new_state, 0) + count) % MOD
            
            # Action 2: Pop element from queue
            if qsize > 0:
                # We need to know which element to pop
                # The element to pop is at position (pushed - qsize)
                pop_idx = pushed - qsize
                new_c = c + B[pop_idx]
                new_state = (pushed, qsize - 1, new_c)
                new_dp[new_state] = (new_dp.get(new_state, 0) + count) % MOD
        
        dp = new_dp
    
    # Count final states where pushed == N, qsize == 0, L <= c <= R
    result = 0
    for (pushed, qsize, c), count in dp.items():
        if pushed == N and qsize == 0 and L <= c <= R:
            result = (result + count) % MOD
    
    print(result)

solve()
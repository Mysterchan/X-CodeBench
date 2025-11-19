def solve():
    MOD = 998244353
    N = int(input())
    s = input().strip()
    
    star_count = s.count('1')
    star_vertices = [i for i in range(N) if s[i] == '1']
    
    # dp[state] = count, where state is a tuple representing in-degrees
    from collections import defaultdict
    
    # We'll build the graph step by step
    # Start with empty in-degrees
    dp = defaultdict(int)
    dp[tuple([0] * (N + 1))] = 1
    
    # Process cycle edges: (i, (i+1) mod N) for i in 0..N-1
    for i in range(N):
        next_i = (i + 1) % N
        new_dp = defaultdict(int)
        
        for state, cnt in dp.items():
            state_list = list(state)
            
            # Option 1: edge goes i -> next_i (next_i gets +1 in-degree)
            new_state = state_list[:]
            new_state[next_i] += 1
            new_dp[tuple(new_state)] = (new_dp[tuple(new_state)] + cnt) % MOD
            
            # Option 2: edge goes next_i -> i (i gets +1 in-degree)
            new_state = state_list[:]
            new_state[i] += 1
            new_dp[tuple(new_state)] = (new_dp[tuple(new_state)] + cnt) % MOD
        
        dp = new_dp
    
    # Process star edges: {i, N} for each i where s[i] = '1'
    for i in star_vertices:
        new_dp = defaultdict(int)
        
        for state, cnt in dp.items():
            state_list = list(state)
            
            # Option 1: edge goes i -> N (N gets +1 in-degree)
            new_state = state_list[:]
            new_state[N] += 1
            new_dp[tuple(new_state)] = (new_dp[tuple(new_state)] + cnt) % MOD
            
            # Option 2: edge goes N -> i (i gets +1 in-degree)
            new_state = state_list[:]
            new_state[i] += 1
            new_dp[tuple(new_state)] = (new_dp[tuple(new_state)] + cnt) % MOD
        
        dp = new_dp
    
    # Count distinct states
    result = len(dp)
    print(result)

solve()
def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = input().strip()
    
    # dp[j][k] = number of strings of length j with LCS exactly k with S
    # We build this incrementally
    
    # Better approach: dp[j][k][i] = strings of length j, LCS k, last match at position i in S
    # But this is complex. Let's use a different formulation.
    
    # dp[j][k] = number of strings of length j where LCS with S is exactly k
    dp = [[0] * (N + 1) for _ in range(M + 1)]
    dp[0][0] = 1
    
    for j in range(M):
        new_dp = [[0] * (N + 1) for _ in range(M + 1)]
        
        for k in range(N + 1):
            if dp[j][k] == 0:
                continue
            
            # Try adding each character
            for c in range(26):
                ch = chr(ord('a') + c)
                
                # Compute new LCS length after adding ch
                # We need to track which characters of S we've matched
                # This requires tracking state of which positions in S we've used
                
                # Actually, we need to track: for each prefix of S, what's the LCS
                # Let's use: dp[j][matched] where matched is a bitmask or list
                pass
    
    # This approach is getting complex. Let me use a different method.
    
    # Use DP with state: dp[j][mask] = number of strings of length j 
    # where mask represents which characters of S have been matched in order
    
    from functools import lru_cache
    
    @lru_cache(maxsize=None)
    def count_strings(pos, s_idx, lcs_len):
        # pos: current position in string being built (0 to M)
        # s_idx: current index in S we're considering
        # lcs_len: current LCS length
        if pos == M:
            return 1 if s_idx == N else 0
        
        result = 0
        for c in range(26):
            ch = chr(ord('a') + c)
            # Check if this character matches any upcoming character in S
            new_s_idx = s_idx
            new_lcs = lcs_len
            
            for i in range(s_idx, N):
                if S[i] == ch:
                    new_s_idx = i + 1
                    new_lcs = lcs_len + 1
                    break
            
            result = (result + count_strings(pos + 1, new_s_idx, new_lcs)) % MOD
        
        return result
    
    # This doesn't track properly either...
    
    # Let me use the proper DP formulation
    # dp[i][j][k] = ways to build string of length i, matched up to S[j], with LCS k
    
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0][0] = 1
    
    for i in range(M):
        for j in range(N + 1):
            for k in range(j + 1):
                if dp[i][j][k] == 0:
                    continue
                
                for c in range(26):
                    ch = chr(ord('a') + c)
                    # Find if ch matches S[j]
                    if j < N and S[j] == ch:
                        dp[i + 1][j + 1][k + 1] = (dp[i + 1][j + 1][k + 1] + dp[i][j][k]) % MOD
                    else:
                        dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % MOD
    
    result = [dp[M][N][k] for k in range(N + 1)]
    print(' '.join(map(str, result)))

solve()
def solve():
    MOD = 998244353
    N, M = map(int, input().split())
    S = input().strip()
    
    # dp[i][j][k] = number of strings of length i that use exactly j positions from S
    # and have LCS exactly k with S[0:j]
    # We need to track which characters in S we've "matched"
    
    # Better approach: dp[pos][matched] = number of ways to build string of length pos
    # where we've matched exactly 'matched' characters from S
    
    # dp[i][j] = number of length-i strings with LCS exactly j with S
    # This is hard to compute directly
    
    # Instead: compute dp[i][j] = number of length-i strings with LCS at least j
    # Then use inclusion-exclusion
    
    # Actually, let's use: dp[m][n][k] = number of strings of length m 
    # where first n chars of S are considered and LCS is exactly k
    
    # Better: for each possible string, compute LCS
    # But 26^M is too large
    
    # Use DP: dp[i][j] = number of strings of length i where LCS with S is exactly j
    
    # Recurrence: if we add character c to string of length i-1:
    # - If c matches S[next_match_pos], LCS can increase by 1
    # - Otherwise, LCS stays same
    
    # Need to track: position in string, position in S we've matched up to, current LCS
    # dp[pos][s_idx][lcs] = count
    
    # dp[pos][s_idx] = number of strings of length pos where we've definitely matched
    # first s_idx characters of S (and possibly more)
    
    # Let's use: dp[m_pos][s_matched] = ways to build string of length m_pos 
    # having matched exactly s_matched characters from S as a subsequence
    
    dp = [[[0] * (N + 1) for _ in range(N + 1)] for _ in range(M + 1)]
    dp[0][0][0] = 1
    
    for i in range(M):
        for j in range(N + 1):
            for k in range(j + 1):
                if dp[i][j][k] == 0:
                    continue
                
                # Add each of 26 characters
                for c_idx in range(26):
                    c = chr(ord('a') + c_idx)
                    
                    # Find next match in S starting from position j
                    next_j = j
                    for idx in range(j, N):
                        if S[idx] == c:
                            next_j = idx + 1
                            break
                    
                    if next_j > j:
                        # We matched a new character from S
                        dp[i + 1][next_j][k + 1] = (dp[i + 1][next_j][k + 1] + dp[i][j][k]) % MOD
                    else:
                        # No new match
                        dp[i + 1][j][k] = (dp[i + 1][j][k] + dp[i][j][k]) % MOD
    
    # Collect answer: sum over all j values for each k
    ans = [0] * (N + 1)
    for j in range(N + 1):
        for k in range(N + 1):
            ans[k] = (ans[k] + dp[M][j][k]) % MOD
    
    print(' '.join(map(str, ans)))

solve()
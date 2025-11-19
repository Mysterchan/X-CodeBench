def solve():
    MOD = 998244353
    
    N, L, R = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    # dp[inserted][removed] = dictionary mapping C values to counts
    dp = [[{} for _ in range(N + 1)] for _ in range(N + 1)]
    dp[0][0][0] = 1
    
    for step in range(2 * N):
        new_dp = [[{} for _ in range(N + 1)] for _ in range(N + 1)]
        
        for inserted in range(N + 1):
            for removed in range(inserted + 1):
                if not dp[inserted][removed]:
                    continue
                    
                for c_val, count in dp[inserted][removed].items():
                    # Action 1: Insert next element
                    if inserted < N:
                        new_c = max(0, c_val - A[inserted])
                        if new_c not in new_dp[inserted + 1][removed]:
                            new_dp[inserted + 1][removed][new_c] = 0
                        new_dp[inserted + 1][removed][new_c] = (
                            new_dp[inserted + 1][removed][new_c] + count
                        ) % MOD
                    
                    # Action 2: Remove first element
                    if removed < inserted:
                        # We need to know which element to remove
                        # The element at position 'removed' in insertion order
                        x = removed
                        new_c = c_val + B[x]
                        if new_c not in new_dp[inserted][removed + 1]:
                            new_dp[inserted][removed + 1][new_c] = 0
                        new_dp[inserted][removed + 1][new_c] = (
                            new_dp[inserted][removed + 1][new_c] + count
                        ) % MOD
        
        dp = new_dp
    
    result = 0
    for c_val, count in dp[N][N].items():
        if L <= c_val <= R:
            result = (result + count) % MOD
    
    print(result)

solve()
MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = input().strip()

    # dp[i][j][k] = number of strings T of length j such that
    # LCS(S[:i], T) = k
    # i in [0..N], j in [0..M], k in [0..min(i,j)]
    # We want dp[N][M][k] for k=0..N

    # Since N <= 10, M <= 100, we can do DP with complexity O(N*M*N)
    # We'll use a 3D DP with dimensions (N+1) x (M+1) x (N+1)

    # Initialize dp with zeros
    dp = [[[0]*(N+1) for _ in range(M+1)] for __ in range(N+1)]
    dp[0][0][0] = 1

    # Precompute powers of 26 for efficiency
    pow26 = [1]*(M+1)
    for i in range(1, M+1):
        pow26[i] = (pow26[i-1]*26) % MOD

    for i in range(N+1):
        for j in range(M+1):
            for k in range(i+1):
                cur = dp[i][j][k]
                if cur == 0:
                    continue
                if j == M:
                    continue
                # We add one character c in 'a'..'z' to T
                # For each c:
                # If i < N and c == S[i], then LCS can increase by 1 if we match S[i]
                # else LCS stays the same or max(k, ...)

                # Count how many letters match S[i] if i < N
                if i < N:
                    # c == S[i]
                    # For c == S[i], LCS can increase by 1: k -> k+1
                    # For other 25 letters, LCS stays k
                    # So:
                    # Add dp[i][j][k] * 1 to dp[i+1][j+1][k+1]
                    # Add dp[i][j][k] * 25 to dp[i][j+1][k]
                    dp[i+1][j+1][k+1] = (dp[i+1][j+1][k+1] + cur) % MOD
                    dp[i][j+1][k] = (dp[i][j+1][k] + cur * 25) % MOD
                else:
                    # i == N, no more characters in S to match
                    # So LCS cannot increase, stays k
                    # Add dp[i][j][k] * 26 to dp[i][j+1][k]
                    dp[i][j+1][k] = (dp[i][j+1][k] + cur * 26) % MOD

    # Now dp[i][M][k] for i=0..N, k=0..i
    # We want sum over i of dp[i][M][k] where i=N (full S processed)
    # But LCS length cannot be more than min(i,j), here j=M, i=N, so max LCS length is N

    # Actually, the dp is constructed so that dp[i][M][k] counts strings T of length M
    # with LCS(S[:i], T) = k, but we want LCS(S, T) = k, i.e. i = N

    # So answer for k is dp[N][M][k]

    # But we must be careful: dp[i][j][k] counts strings T of length j with LCS(S[:i], T) = k
    # For i < N, dp[i][M][k] counts strings T with LCS(S[:i], T) = k, but not full S
    # We want only dp[N][M][k]

    # So output dp[N][M][k] for k=0..N

    # However, the above DP counts strings T with LCS(S[:i], T) = k, but we must ensure
    # that the LCS with full S is exactly k. The DP is constructed so that at i=N,
    # dp[N][M][k] counts strings T with LCS(S, T) = k.

    # So final answer is dp[N][M][k] for k=0..N

    # Output answers
    ans = [dp[N][M][k] % MOD for k in range(N+1)]
    print(*ans)

if __name__ == "__main__":
    main()
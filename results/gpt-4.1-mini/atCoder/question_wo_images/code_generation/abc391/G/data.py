MOD = 998244353

def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    S = input().strip()

    # dp[i][j][k]: number of strings T of length j such that
    # LCS(S[:i], T) = k
    # i in [0..N], j in [0..M], k in [0..i]
    # We only need dp for current j, so we can optimize memory.

    # Initialize dp arrays
    # dp[i][k]: number of strings T of length current_j with LCS(S[:i], T) = k
    dp_prev = [[0]*(N+1) for _ in range(N+1)]
    dp_prev[0][0] = 1  # empty S prefix and empty T prefix, LCS=0

    for length in range(1, M+1):
        dp_curr = [[0]*(N+1) for _ in range(N+1)]
        for i in range(N+1):
            for k in range(i+1):
                val = dp_prev[i][k]
                if val == 0:
                    continue
                # For next character c in 'a'..'z'
                # We consider all 26 letters
                # For each letter, we update dp_curr accordingly

                # Count how many letters c satisfy:
                # If i < N and c == S[i], then LCS can increase by 1 (k->k+1)
                # else LCS stays k

                # Number of letters equal to S[i] if i < N: 1
                # Number of letters not equal to S[i]: 25

                if i < N:
                    # c == S[i]
                    dp_curr[i+1][k+1] = (dp_curr[i+1][k+1] + val) % MOD
                    # c != S[i]
                    dp_curr[i][k] = (dp_curr[i][k] + val * 25) % MOD
                else:
                    # i == N, no more chars in S to match
                    # all 26 letters keep LCS=k
                    dp_curr[i][k] = (dp_curr[i][k] + val * 26) % MOD
        dp_prev = dp_curr

    # After processing all M characters, dp_prev[N][k] is number of strings T of length M
    # with LCS(S, T) = k

    # But dp_prev[i][k] for i < N also exist, but we want full S (i=N)
    # So answer is dp_prev[N][k] for k=0..N

    # However, dp_prev[N][k] might be zero for k > N, but k <= N anyway.

    # Print answers for k=0..N
    ans = [dp_prev[N][k] % MOD for k in range(N+1)]
    print(*ans)

if __name__ == "__main__":
    main()
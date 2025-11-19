MOD = 998244353

def main():
    import sys
    sys.setrecursionlimit(10**7)
    N, M = map(int, sys.stdin.readline().split())
    S = sys.stdin.readline().strip()

    # dp[i][j][k]: number of length-j strings whose LCS with S[:i] is exactly k
    # i in [0..N], j in [0..M], k in [0..i]
    # We'll build dp for i from 0 to N
    # Base case: dp[0][0][0] = 1 (empty string vs empty prefix)
    # For i=0, dp[0][j][0] = 26^j (all strings of length j have LCS=0 with empty S)
    # For i>0, we use transitions based on character matches

    # Precompute powers of 26
    pow26 = [1]*(M+1)
    for x in range(1, M+1):
        pow26[x] = pow26[x-1]*26 % MOD

    # Initialize dp arrays
    # We'll keep dp for previous i and current i to save memory
    prev = [[0]*(N+1) for _ in range(M+1)]
    # For i=0, LCS length can only be 0
    for j in range(M+1):
        prev[j][0] = pow26[j]

    for i in range(1, N+1):
        curr = [[0]*(i+1) for _ in range(M+1)]
        c = S[i-1]
        for j in range(M+1):
            for k in range(i+1):
                if k > j or k > i:
                    # impossible to have LCS length k if k>j or k>i
                    continue
                if j == 0:
                    # length 0 string, LCS length 0 only
                    if k == 0:
                        curr[j][k] = 1
                    else:
                        curr[j][k] = 0
                    continue

                # Transition:
                # We consider the last character of the length-j string
                # Two cases:
                # 1) last char != S[i-1]:
                #    then LCS length k remains same as dp[i][j-1][k]
                #    number of such chars: 25 (all except c)
                # 2) last char == S[i-1]:
                #    then LCS length k = dp[i-1][j-1][k-1]
                #    number of such chars: 1

                res = 0
                if k <= i-1 and k <= j-1:
                    # last char == c, increase LCS by 1
                    res += prev[j-1][k-1] if k-1 >= 0 else 0
                # last char != c, LCS length unchanged
                res += prev[j-1][k]*25 if k <= i else 0

                curr[j][k] = res % MOD
        prev = curr

    # Now prev is dp[N]
    # prev[j][k]: number of length-j strings with LCS exactly k with S[:N]
    # We want dp[N][M][k] for k=0..N
    ans = [prev[M][k] if k <= N else 0 for k in range(N+1)]
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    main()
import sys
input = sys.stdin.readline

mod = 998244353

def power(a, b):
    res = 1
    while b > 0:
        if b % 2 == 1:
            res = res * a % mod
        a = a * a % mod
        b >>= 1
    return res

def solve():
    N, M = map(int, input().split())
    S = input().strip()
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for i in range(26):
        c = chr(ord('a') + i)
        for j in range(N):
            for k in range(M):
                if S[j] == c:
                    dp[j + 1][k + 1] += dp[j][k]
                    dp[j + 1][k + 1] %= mod
                else:
                    dp[j][k + 1] += dp[j][k] * 25
                    dp[j][k + 1] %= mod

    ans = [0] * (N + 1)
    for i in range(N + 1):
        for j in range(M + 1):
            if j >= i:
                ans[i] += dp[N][j] * power(26, M - j)
                ans[i] %= mod

    print(*ans)

solve()
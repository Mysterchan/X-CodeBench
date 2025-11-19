M = 1010
is_prime = [1] * M
is_prime[0] = is_prime[1] = 0
primes = []
for p in range(2, M):
    if is_prime[p]:
        for q in range(2 * p, M, p):
            is_prime[q] = 0
        primes.append(p)

MOD = 998244353
N = int(input())
A = list(map(int, input().split()))
ans = 1
for p in primes:
    c = [0] * (N - 1)
    for i in range(N - 1):
        q = p
        while A[i] % q == 0:
            c[i] += 1
            q *= p
    s = sum(c)
    if s == 0:
        continue
    pows = [1] * (s + 1)
    for i in range(1, s + 1):
        pows[i] = (pows[i - 1] * p) % MOD

    dp = [[0, 0] for _ in range(s + 1)]
    dp[0][1] = 1
    for i in range(1, s + 1):
        dp[i][0] = pows[i]

    for i in range(N - 1):
        ndp = [[0, 0] for _ in range(s + 1)]
        for j in range(s + 1):
            if c[i] == 0:
                ndp[j][0] += dp[j][0] * pows[j]
                ndp[j][0] %= MOD
                ndp[j][1] += dp[j][1] * pows[j]
                ndp[j][1] %= MOD
            else:
                if j - c[i] == 0:
                    ndp[j - c[i]][1] += sum(dp[j]) * pows[j - c[i]]
                    ndp[j - c[i]][1] %= MOD
                elif j - c[i] > 0:
                    ndp[j - c[i]][0] += dp[j][0] * pows[j - c[i]]
                    ndp[j - c[i]][0] %= MOD
                    ndp[j - c[i]][1] += dp[j][1] * pows[j - c[i]]
                    ndp[j - c[i]][1] %= MOD
                if j + c[i] <= s:
                    ndp[j + c[i]][0] += dp[j][0] * pows[j + c[i]]
                    ndp[j + c[i]][0] %= MOD
                    ndp[j + c[i]][1] += dp[j][1] * pows[j + c[i]]
                    ndp[j + c[i]][1] %= MOD
        dp = ndp

    res = 0
    for i in range(s + 1):
        res += dp[i][1]
        res %= MOD
    ans *= res
    ans %= MOD

print(ans)
N,A,B = map(int,input().split())
Q = int(input())
K = list(map(int,input().split()))
MOD = 998244353

MAXN = 10**7 + 5
fac = [1,1] + [0]*MAXN
finv = [1,1] + [0]*MAXN
inv = [0,1] + [0]*MAXN
for i in range(2,MAXN+2):
    fac[i] = fac[i-1] * i % MOD
    inv[i] = -inv[MOD%i] * (MOD // i) % MOD
    finv[i] = finv[i-1] * inv[i] % MOD

def comb(n,r):
    if n < r: return 0
    if n < 0 or r < 0: return 0
    return fac[n] * (finv[r] * finv[n-r] % MOD) % MOD

def solve_1d(n, a):
    ret = [0] * (n+1)
    ret[n] = 1
    for i in reversed(range(1,n)):
        ret[i] = ret[i+1] * 2
        ret[i] -= comb(n-i-1, a)
        ret[i] -= comb(n-i-1, n-1-a)
        ret[i] %= MOD
    pow2 = 1
    for i in range(1, n+1):
        ret[i] *= pow2
        ret[i] %= MOD
        pow2 = pow2 * 2 % MOD
    return ret

X = solve_1d(N, A-1)
Y = solve_1d(N, B-1)
for k in K:
    ans = X[k] * Y[k] - X[k-1] * Y[k-1]
    ans %= MOD
    print(ans)
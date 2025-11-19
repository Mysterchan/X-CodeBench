import sys
input = sys.stdin.readline

MOD = 998244353

def comb(n, r):
    return fact[n] * inv[r] % MOD * inv[n-r] % MOD if n >= r >= 0 else 0

def qpow(a, b):
    res = 1
    while b:
        if b & 1:
            res = res * a % MOD
        a = a * a % MOD
        b >>= 1
    return res

def init():
    global fact, inv
    fact = [1]
    for i in range(1, 4*10**5+10):
        fact.append(fact[-1] * i % MOD)
    inv = [qpow(fact[-1], MOD-2)]
    for i in range(4*10**5+9, 0, -1):
        inv.append(inv[-1] * i % MOD)
    inv.reverse()

def main():
    init()
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    Q, sh, sw = map(int, input().split())
    sh -= 1
    sw -= 1
    dp = [[0]*W for _ in range(H)]
    dp[0][0] = A[0][0]
    for i in range(1, H):
        dp[i][0] = dp[i-1][0] * A[i][0] % MOD
    for i in range(1, W):
        dp[0][i] = dp[0][i-1] * A[0][i] % MOD
    for i in range(1, H):
        for j in range(1, W):
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) * A[i][j] % MOD
    ans = [0]*Q
    for i in range(Q):
        d, a = input().split()
        a = int(a)
        if d == 'L' and sw:
            sw -= 1
        elif d == 'R' and sw < W-1:
            sw += 1
        elif d == 'U' and sh:
            sh -= 1
        elif d == 'D' and sh < H-1:
            sh += 1
        A[sh][sw] = a
        dp[sh][sw] = a
        if sh:
            dp[sh][sw] = (dp[sh][sw] + dp[sh-1][sw]) % MOD
        if sw:
            dp[sh][sw] = (dp[sh][sw] + dp[sh][sw-1]) % MOD
        for x in range(sh+1, H):
            dp[x][sw] = (dp[x-1][sw] * a + dp[x][sw]) % MOD
        for y in range(sw+1, W):
            dp[sh][y] = (dp[sh][y-1] * a + dp[sh][y]) % MOD
        for x in range(sh+1, H):
            for y in range(sw+1, W):
                dp[x][y] = (dp[x-1][y] + dp[x][y-1]) * a % MOD
        ans[i] = dp[H-1][W-1] * comb(H+W-2, H-1) % MOD
    print(*ans, sep='\n')

main()
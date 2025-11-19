import sys
input = sys.stdin.readline

mod = 998244353

class Comb:
    __slots__ = ["fac", "finv", "mod"]
    def __init__(self, lim:int, mod:int = mod):
        self.fac = [1]*(lim+1)
        self.finv = [1]*(lim+1)
        self.mod = mod
        for i in range(2,lim+1):
            self.fac[i] = self.fac[i-1]*i%self.mod
        self.finv[lim] = pow(self.fac[lim],-1,mod)
        for i in range(lim,2,-1):
            self.finv[i-1] = self.finv[i]*i%self.mod

    def C(self, a, b):
        if b < 0 or a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[b]%self.mod*self.finv[a-b]%self.mod

h, w = map(int, input().split())
if h < w:
    h, w = w, h

comb = Comb(w + 10)

dp = [[0] * (w + 1) for _ in range(h + 2)]
cnt = [[0] * (w + 1) for _ in range(h + 2)]
cnt[0][0] = 1

for i in range(h):
    # Precompute binomial coefficients for this row
    binom = [[0] * (w + 2) for _ in range(w + 2)]
    for j in range(w + 1):
        for k in range(w + 2):
            binom[j][k] = comb.C(k + j, j)
    
    for j in range(w + 1):
        if cnt[i][j] == 0:
            continue
        
        cnt_val = cnt[i][j]
        dp_val = dp[i][j]
        
        # Accumulate contributions for all k at once
        for k in range(w + 1 - j):
            idx = k + j
            
            b1 = binom[j][k + j + 1]
            b2 = binom[j-1][k + j + 1] if j > 0 else 0
            
            cnt[i+1][idx] = (cnt[i+1][idx] + cnt_val * b1) % mod
            dp[i+1][idx] = (dp[i+1][idx] + dp_val * b1 + cnt_val * (k * i * b1 + b2)) % mod

ans = 0
for j in range(w + 1):
    c = comb.C(w, j)
    ans = (ans + dp[h][j] * c + cnt[h][j] * h * (w - j) % mod * c) % mod

print(ans)
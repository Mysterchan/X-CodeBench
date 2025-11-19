mod=998244353
class Comb:
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
        assert b >= 0, "The second argument is negative."
        if a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[b]%self.mod*self.finv[a-b]%self.mod

    def P(self, a, b):
        assert b >= 0, "The second argument is negative."
        if a < b: return 0
        if a < 0: return 0
        return self.fac[a]*self.finv[a-b]%self.mod

    def H(self, a, b): return self.C(a+b-1,b)
    def F(self, a): return self.fac[a]
    def Fi(self, a): return self.finv[a]

N=int(input())
S=input()
n = 6000
cmb = Comb(n, mod)
c = [0 for _ in range(N+1)]
d = 0
ans = 1
c[0] += 1
for i in range(N):
    if S[i] == "(":
        d += 1
    else:
        ans *= cmb.F(c[d]-1)
        ans%=mod
        c[d] = 0
        d -= 1
    c[d]+=1
ans *= cmb.F(c[0]-1)
ans%=mod
print(ans)
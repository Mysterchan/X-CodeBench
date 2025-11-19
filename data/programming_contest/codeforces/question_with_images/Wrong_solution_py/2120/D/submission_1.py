MOD=10**9+7

def C(n,a,mod=MOD):
    res=1
    for i in range(1,a+1):
        res=res*(n-i+1)%mod
        res=res*pow(i,mod-2,mod)%mod
    return res

def solve():
    a,b,k=map(int,input().split())
    n=k*(a-1)+1
    comb=C(n,a,MOD)
    m=((n-1)*k%MOD*comb%MOD+1)%MOD
    print(n%MOD,m)

T=int(input())
for _ in range(T):
    solve()

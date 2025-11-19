import sys
readline = sys.stdin.readline

MOD = 998244353

M = 2*10**5+1
g = [0]*M
for i in range(1,M):
    g[i] = (g[i-1]*10+1)%MOD
g[0] = 1

def Eratosthenes(N):
    N+=1
    is_prime_list = [True]*N
    m = int(N**0.5)+1
    for i in range(3,m,2):
        if is_prime_list[i]:
            is_prime_list[i*i::2*i]=[False]*((N-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,N,2) if is_prime_list[i]]

primes = Eratosthenes(M)

yaku = [[] for _ in range(M)]
for p in primes:
    for v in range(p,M,p):
        yaku[v].append(p)

for p in primes:
    for i in range((M-1)//p,0,-1):
        g[p*i] *= pow(g[i],-1,MOD)
        g[p*i] %= MOD

n = int(readline())
*a, = map(int,readline().split())

ans = 1
used = [0]*M
for ai in a:
    if not used[ai]:
        ans = ans*g[ai]%MOD
        used[ai] = 1
        st = [ai]
        while st:
            w = st.pop()
            for v in yaku[w]:
                nv = w//v
                if used[nv] == 0:

                    used[nv] = 1
                    ans = ans*g[nv]%MOD
                    st.append(nv)
    print(ans)
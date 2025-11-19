N,M = map(int,input().split())
graph=[[0]*N for _ in range(N)]
mod =998244353
for i in range(M):
    U,V = map(lambda x:int(x)-1, input().split())
    graph[U][V]+=1
    graph[V][U]+=1

ans=0

for s in range(2,N):
    DP = [[0]*(s+1) for _ in range(1<<(s+1))]
    DP[1<<s][s]=1
    for bit in range(1<<s,1<<(s+1)):
        for i in range(s+1):
            if (bit>>i) &1:
                for j in range(s):
                    if (bit>>j) &1:
                        continue
                    DP[bit | (1<<j)][j] += DP[bit][i]*graph[i][j]
                    DP[bit | (1<<j)][j] %= mod
    for i in range(s):
        DP[(1<<s) | (1<<i)][i]-=graph[i][s]
    for bit in range(1<<s, 1<<(s+1)):
        for i in range(s):
            if (bit>>i) &1:
                ans += DP[bit][i]*graph[i][s]
                ans %= mod

ans =(ans*pow(2,-1,mod))%mod

for i in range(N-1):
    for j in range(i+1,N):
        ans = (ans+graph[i][j]*(graph[i][j]-1)//2)%mod
print(ans)
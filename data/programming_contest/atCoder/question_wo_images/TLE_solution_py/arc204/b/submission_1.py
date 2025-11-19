n,k=map(int,input().split())
P=[int(x)-1 for x in input().split()]
vis=[1]*(n*k)
ans=0
for i in range(n*k):
    if vis[i]:
        S=[i%n]
        vis[i]=0
        j=P[i]
        while j!=i:
            vis[j]=0
            S.append(j%n)
            j=P[j]
        if len(S)==1:
            continue
        m=len(S)
        dp=[[0]*m for _ in range(m)]
        for i in range(m-1):
            dp[i][i+1]=S[i]==S[i+1]
        for i in range(m)[::-1]:
            for j in range(i+2,m):
                dp[i][j]=max(dp[i][j-1],dp[i+1][j])+(S[i]==S[j])
                for a in range(i+1,j):
                    dp[i][j]=max(dp[i][j],dp[i][a]+dp[a][j])
        ans+=dp[0][-1]
print(ans)
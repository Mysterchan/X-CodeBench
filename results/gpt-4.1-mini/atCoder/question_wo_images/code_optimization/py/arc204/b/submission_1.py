n,k=map(int,input().split())
P=[int(x)-1 for x in input().split()]
vis=[True]*(n*k)
ans=0
for i in range(n*k):
    if vis[i]:
        S=[]
        cur=i
        while vis[cur]:
            vis[cur]=False
            S.append(cur%n)
            cur=P[cur]
        if len(S)==1:
            continue
        m=len(S)
        dp=[0]*m
        for length in range(2,m+1):
            new_dp=[0]*m
            for start in range(m-length+1):
                end=start+length-1
                res=max(dp[start],dp[start+1])
                if S[start]==S[end]:
                    res=max(res,dp[start+1]+1)
                for mid in range(start+1,end):
                    val=dp[start]+dp[mid]
                    if val>res:
                        res=val
                new_dp[start]=res
            dp=new_dp
        ans+=dp[0]
print(ans)
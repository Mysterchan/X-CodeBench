from collections import defaultdict

def solve():
    N,W = map(int,input().split())
    P = [[] for _ in range(60)]
    for i in range(N):
        X,Y = map(int,input().split())
        P[X].append(Y)

    S = [[0] for _ in range(60)]
    for x in range(60):
        P[x].sort(reverse=True)
        for k in range(len(P[x])):
            S[x].append(S[x][-1]+P[x][k])

    dp = [defaultdict(int) for _ in range(60)]
    dp[0][W] = 0
    for x in range(59):
        for v,w in dp[x].items():
            for i in range(len(S[x])):
                if v-i >= 0:
                    dp[x+1][(v-i)//2] = max(dp[x+1][(v-i)//2], w+S[x][i])

    ans = max(dp[59].values())
    print(ans)

T = int(input())
for i in range(T):
    solve()
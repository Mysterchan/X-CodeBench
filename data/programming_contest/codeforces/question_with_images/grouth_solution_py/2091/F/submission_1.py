import math
rn = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rs = lambda: input()
mn = 998244353
for _ in range(rn()):
    n, m, d = rl()
    mh = []
    for i in range(n):
        mh.append(rs())
    dp1, dp2 = [0]*(m+1), [0]*(m+1)
    r = d-1
    for i in range(n-1, -1, -1):
        if i == n-1:
            for j in range(1, m+1):
                if mh[i][j-1] == 'X':
                    dp1[j] = 1
        else:
            for j in range(1,m+1):
                dp2[j] = (dp2[j-1]+dp2[j])%mn
            for j in range(1, m+1):
                if mh[i][j-1] == 'X':
                    dp1[j] = (dp2[min(m, j+r)]+mn-dp2[max(0, j-r-1)])%mn
                else:
                    dp1[j] = 0
        for j in range(1,m+1):
            dp1[j] = (dp1[j-1]+dp1[j])%mn
        for j in range(1,m+1):
            if mh[i][j-1] == 'X':
                dp2[j] = (mn+dp1[min(m, j+d)]-dp1[max(0, j-d-1)])%mn
            else:
                dp2[j] = 0
    print(sum(dp2)%mn)


t = int(input())
for _ in range(t):
    n, m= map(int, input().split())
    a = [list(map(int, input().strip().split())) for i in range(n)]
    mx = max(max(i)for i in a)
    row = [0]*n
    col = [0]*m
    cnt = 0

    for i in range(n):
        for j in range(m):
            if a[i][j]==mx:
                cnt+=1
                row[i]+=1
                col[j]+=1
    ans = mx

    for i in range(n):
        for j in range(m):
            if (row[i]+col[j]-int(a[i][j]==mx))==cnt:
                ans = mx-1
    print(ans)
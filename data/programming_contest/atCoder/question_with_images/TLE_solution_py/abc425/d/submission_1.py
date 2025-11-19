H,W = map(int,input().split())
S = [list(input()) for i in range(H)]
ans = 0
for i in range(H):
    for j in range(W):
        if S[i][j] == '#':
            ans+=1
            S[i][j] = 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
l = 1
while(True):
    lastans = ans
    for i in range(H):
        for j in range(W):
            if S[i][j] != '.':
                continue
            tmp = 0
            for k in range(4):
                nx = j+dx[k];ny =i+dy[k]
                if 0>nx or nx>=W or ny<0 or ny>=H:
                    continue
                if S[ny][nx] != '.' and S[ny][nx]!=l:
                    tmp+=1
            if tmp==1:
                S[i][j] = l
                ans += 1
    if lastans == ans:
        break
    l+=1
print(ans)
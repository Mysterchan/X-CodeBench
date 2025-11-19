N,R,C = map(int,input().split())
S = input().strip()

dx = {'N':-1,'S':1,'W':0,'E':0}
dy = {'N':0,'S':0,'W':-1,'E':1}

seen = {(0,0)}
x = y = 0
out = []

for ch in S:
    x += dx[ch]
    y += dy[ch]
    if (x,y) not in seen:
        seen.add((x,y))
    if (x - R,y - C) in seen:
        out.append(1)
    else:
        out.append(0)
print(*out,sep="")
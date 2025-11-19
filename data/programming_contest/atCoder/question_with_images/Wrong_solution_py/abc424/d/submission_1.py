import sys
sys.setrecursionlimit(10*9)

def dfs(SS,y,x,cnt):
    global ans
    for y in range(y,H - 1):
        for x in range(x,W - 1):
            if SS[y][x] == SS[y + 1][x] == SS[y][x + 1] == SS[y+1][x+1] == "#":
                S1 = [s[:]for s in SS]
                S2 = [s[:]for s in SS]
                S1[y + 1][x] = "."
                S2[y + 1][x + 1] = "."
                ty = y
                tx = x
                if tx == W - 2:
                    ty += 1
                    tx = 0
                else:
                    tx += 1
                cnt = min(dfs(S1,ty,tx,cnt + 1),dfs(S2,ty,tx,cnt + 1))

    ans = min(ans,cnt)
    return cnt

T = int(input())
for _ in range(T):
    H, W = map(int,input().split())
    S = [list(input())for _ in range(H)]
    ans = 10**10
    dfs(S,0,0,0)

    print(ans)
from collections import deque
q=deque()

t=int(input())

for i in range(t):
    h,w=map(int,input().split())
    s=input()
    n=len(s)
    seen=[[False for _ in range(w)] for _ in range(h)]
    rr=0
    dd=0
    for i in range(n):
        if s[i]=='R':
            rr+=1
        elif s[i]=='D':
            dd+=1
    r=w-rr-1
    d=h-dd-1
    ans=1

    q.append((0,0,r,d))
    seen[0][0]=True

    while q:
        row,col,rk,dk=q.popleft()

        if row==h-1 and col==w-1:
            continue

        if s[row+col]=='R' and not seen[row][col+1]:
            q.append((row,col+1,rk,dk))
            seen[row][col+1]=True
            ans+=1
        elif s[row+col]=='D' and not seen[row+1][col]:
            seen[row+1][col]=True
            q.append((row+1,col,rk,dk))
            ans+=1
        else:
            if rk>0 and not seen[row][col+1]:
                q.append((row,col+1,rk-1,dk))
                seen[row][col+1]=True
                ans+=1
            if dk>0 and not seen[row+1][col]:
                seen[row+1][col]=True
                q.append((row+1,col,rk,dk-1))
                ans+=1
    print(ans)
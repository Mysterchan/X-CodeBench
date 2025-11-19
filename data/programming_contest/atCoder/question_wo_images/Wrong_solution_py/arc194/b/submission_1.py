from collections import deque

def calc(x):
    a,b = x,pos[x]

    return (a+b-1)*abs(b-a)//2

def calc2(x,i):
    return (x+i-1)*(x-i)//2

N = int(input())
P = [0] + list(map(int, input().split()))
pos = {v:i for i,v in enumerate(P)}

ans = 0
q = deque()
for i in range(N,-1,-1):
    if P[i] - len(q) < i:
        q.append(P[i])
    if len(q)>0 and q[0] == i:
        q.popleft()
        while len(q)>0 and q[0]>i:
            q.popleft()

    ans += (i-1)*len(q)
print(ans)
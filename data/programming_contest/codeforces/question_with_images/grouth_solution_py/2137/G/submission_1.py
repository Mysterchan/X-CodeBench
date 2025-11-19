import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n,m,q = map(int,input().split())
    G = [[] for _ in range(n+1)]
    A = [1 for _ in range(n+1)]
    B = [0 for _ in range(n+1)]
    C = [0 for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int,input().split())
        G[b].append(a)
        C[a] += 1
    for _ in range(q):
        a,b = map(int,input().split())
        if a == 2:
            if A[b]: print("yes")
            else: print("no")
        else:
            q = []
            if A[b] == 1: q.append((b,0))
            if B[b] == 0: q.append((b,1)); B[b] = 1
            for x,t in q:
                if t:
                    for c in G[x]:
                        C[c] -= 1
                        if C[c] == 0:
                           q.append((c,0))
                else:
                    if A[x] == 0: continue
                    A[x] = 0
                    for c in G[x]:
                        if B[c]: continue
                        B[c] = 1
                        q.append((c,1))

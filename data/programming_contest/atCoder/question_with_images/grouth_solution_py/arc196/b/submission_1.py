Q=int(input())
for _ in range(Q):
    H,W=map(int,input().split())
    T=[input() for i in range(H)]
    G=[[] for i in range(2*H*W)]
    for a in range(H):
        for b in range(W):
            c,d=a,(b+1)%W
            w1,w2=a*W+b,c*W+d
            if T[a][b]=='B':
                G[2*w1].append((2*w2,0))
                G[2*w2].append((2*w1,0))
                G[2*w1].append((2*w1+1,1))
                G[2*w1+1].append((2*w1,1))
            else:
                G[2*w1].append((2*w2,1))
                G[2*w2].append((2*w1,1))
    for a in range(H):
        for b in range(W):
            c,d=(a+1)%H,b
            w1,w2=a*W+b,c*W+d
            if T[a][b]=='B':
                G[2*w1+1].append((2*w2+1,0))
                G[2*w2+1].append((2*w1+1,0))
            else:
                G[2*w1+1].append((2*w2+1,1))
                G[2*w2+1].append((2*w1+1,1))
    ans=True
    dist=[-1]*(2*H*W)
    from collections import deque
    result=1
    mod=998244353
    for i in range(2*H*W):
        if dist[i]==-1:
            dist[i]=0
            S=deque()
            S.append(i)
            while S:
                if ans==False:
                    break
                x=S.pop()
                for B in G[x]:
                    y,t=B[:]
                    if dist[y]==-1:
                        dist[y]=(dist[x]+t)%2
                        S.append(y)
                    else:
                        if dist[y]!=(dist[x]+t)%2:
                            ans=False
                            break
            if ans==False:
                result=0
            else:
                result*=2
                result%=mod
    print(result)
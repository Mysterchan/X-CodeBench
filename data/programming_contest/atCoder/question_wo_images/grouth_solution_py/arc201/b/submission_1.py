t=int(input())
for _ in range(t):
    n,w=map(int,input().split())
    A=[[] for _ in range(60)]
    for i in range(n):
        x,y=map(int,input().split())
        A[x].append(y)
    ans=0
    for i in range(60):
        A[i].sort()
        if w&1 and A[i]:
            ans+=A[i][-1]
            A[i].pop()
        if i<59:
            for j in range(0,len(A[i])-1,2)[::-1]:
                A[i+1].append(A[i].pop()+A[i].pop())
            if A[i]:
                A[i+1].append(A[i].pop())
        w//=2
    print(ans)
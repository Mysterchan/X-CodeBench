N,X,Y=map(int,input().split())
S=list(map(int,list(input())))
T=list(map(int,list(input())))

r0=0
b=None
r1=0

for i in range(N):
    if S[i]==0:
        if b!=0:
            b=0
            r0=0
        r0+=1
    else:
        b=1
        r1+=1
        if r0>=X and r1==Y:
            r1=0
            bx=(r0//X)*X
            for j in range(i-Y+1,i+1):
                S[j-bx]=1
                S[j]=0
            r0=bx
            b=0

r0=0
b=None
r1=0

for i in range(N):
    if T[i]==0:
        r1=0
        if b!=0:
            b=0
            r0=0
        r0+=1
    else:
        b=1
        r1+=1
        if r0>=X and r1==Y:
            r1=0
            bx=(r0//X)*X
            for j in range(i-Y+1,i+1):
                T[j-bx]=1
                T[j]=0
            r0=bx
            b=0

if S==T:
    print('Yes')
else:
    print('No')
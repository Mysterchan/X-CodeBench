import sys
input=sys.stdin.readline
M=998244353
N,X,Y=map(int,input().split())
C=[0,0,0]

# Precompute factorials and inverses for combinations
maxN=N*2+10
F=[1]*(maxN)
for i in range(1,maxN):
    F[i]=F[i-1]*i%M
G=[1]*(maxN)
G[-1]=pow(F[-1],M-2,M)
for i in range(maxN-2,-1,-1):
    G[i]=G[i+1]*(i+1)%M
c=lambda n,r:0 if r>n or r<0 else F[n]*G[r]%M*G[n-r]%M

for _ in range(N):
    a,b=map(int,input().split())
    b%=2
    if (Y*(X+1))%2:
        if a-b>=1:
            C[0]+=1
        elif b:
            C[1]+=1
        else:
            C[2]+=1
    elif (X*(Y+1))%2:
        if a+b<1:
            C[2]+=1
        elif a<2 and b:
            C[1]+=1
        else:
            C[0]+=1
    else:
        val = [a%2 - b, b][(X*Y)%2]
        C[2 - bool(val)] += 1

# Precompute prefix sums Q for category 1
max_i = C[1]*2+1
Q = [0]*(max_i+1)
for i in range(max_i):
    if i%2==0:
        Q[i+1] = (Q[i] + c(C[1], i//2))%M
    else:
        Q[i+1] = Q[i]

res=0
x_mod = (X*(Y+1))%2
for i in range(C[0]+1):
    idx = max(0, C[1] + C[0]*x_mod + 1 - i)
    if idx > max_i:
        idx = max_i
    val = (c(C[0], i) * (Q[max_i] - Q[idx]) )%M
    res = (res + val)%M

res = (res * pow(2, C[2], M))%M
print(res)
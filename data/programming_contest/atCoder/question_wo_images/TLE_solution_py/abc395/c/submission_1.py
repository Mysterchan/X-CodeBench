N = int(input())
A = list(map(int, input().split()))
L = []

for i in range (N-1):
    for j in range (i+1,N):
        if A[i]==A[j]:
            L.append(j-i+1)

if L==[]:
    ans=-1
else:
    ans=min(L)

print(ans)
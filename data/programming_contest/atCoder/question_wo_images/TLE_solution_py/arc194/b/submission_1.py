N = int(input())
P = list(map(int, input().split()))
id = [-1] * N
for i in range(N):
    id[P[i]-1] = i

ans = 0
for i in reversed(range(N)):
    if id[i] == i:
        continue

    while i > id[i]:
        ans += id[i]+1
        a,b = id[i],id[i]+1
        id[P[a]-1],id[P[b]-1] = id[P[b]-1],id[P[a]-1]
        P[a],P[b] = P[b],P[a]
print(ans)
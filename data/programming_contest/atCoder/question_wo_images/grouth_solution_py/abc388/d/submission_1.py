N = int(input())
A = list(map(int,input().split()))
imos = [0]*(N+2)

ruiseki = 0
ans = [0] * N

for t in range(1,N+1):
    ruiseki += imos[t]
    S = A[t-1] + ruiseki

    ans[t - 1] = max(0,S - (N - t))

    L = min(S,N - t)
    if L > 0:
        imos[t+1] += 1
        imos[t + L + 1] -= 1
print(*ans)
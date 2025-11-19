N, M = map(int, input().split())
AB = [0] * (N + 1)
for i in range(M):
    ab = list(map(int, input().split()))
    if ab[0] == 2 and ab[1] == N:
        AB[0] += 1
    else:
        d1 = ab[0] - 1
        d2 = N + 1 - ab[1]
        if d1 == d2:
            AB[0] += 1
        elif d1 < d2:
            d3 = ab[1] + d1
            AB[d3] += 1
        else:
            d3 = ab[0] - d2
            AB[d3] += 1
ans = 0

for i in range(len(AB) - 1):
    ans += AB[i] * sum(AB[i + 1:])
print(ans)
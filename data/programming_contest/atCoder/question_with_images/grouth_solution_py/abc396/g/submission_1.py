H, W = (int(x) for x in input().split())
A = [int(input(), 2) for _ in range(H)]

dp = [[0] * (1 << W) for _ in range(W + 1)]
for a in A:
    dp[0][a] += 1

for i in range(W):
    for j in range(i, -1, -1):
        for k in range(1 << W):
            dp[j + 1][k ^ 1 << i] += dp[j][k]

result = H * W
for k in range(1 << W):
    count = 0
    for i in range(W + 1):
        count += dp[i][k] * min(i, W - i)
    result = min(result, count)

print(result)
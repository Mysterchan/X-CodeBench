H, W = map(int, input().split())

row_count = [0] * (1 << W)
for _ in range(H):
    s = input().strip()
    mask = int(s, 2)
    row_count[mask] += 1

dp = [[0] * (1 << W) for _ in range(W + 1)]
dp[0] = row_count[:]

for bit in range(W):
    for c in range(1, W + 1):
        for X in range(1 << W):
            dp[c][X^(1<<bit)] += dp[c - 1][X ]

ans = 10**18
for X in range(1 << W):
    total_cost = 0
    for c in range(W + 1):
        total_cost += dp[c][X] * min(c, W - c)
    ans = min(ans, total_cost)

print(ans)
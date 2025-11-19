H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

total_sum = sum(sum(row) for row in A)
min_value = min(min(row) for row in A)

if min_value >= 0:
    print(total_sum)
    exit()

# The maximum number of domino placements we can make
# Essentially, we want to find how much we can reduce the score
rows = H
cols = W
dp = [[0] * W for _ in range(H)]

for i in range(H):
    for j in range(W):
        dp[i][j] = A[i][j]

# We try to calculate the minimum score we can end up with
for i in range(H):
    for j in range(W):
        if j < W - 1:  # can place horizontally
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + A[i][j + 1])
        if i < H - 1:  # can place vertically
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + A[i + 1][j])

# The maximum score we can have without covering cells
max_score = max(dp[i][j] for i in range(H) for j in range(W))
print(total_sum - max_score)
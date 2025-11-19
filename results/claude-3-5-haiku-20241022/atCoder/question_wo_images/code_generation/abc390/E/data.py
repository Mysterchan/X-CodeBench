N, X = map(int, input().split())

# Separate foods by vitamin type
foods = [[], [], []]
for _ in range(N):
    v, a, c = map(int, input().split())
    foods[v-1].append((a, c))

# For each vitamin type, compute max vitamin for each calorie budget
# dp[v][c] = max vitamin v we can get with at most c calories
dp = [[0] * (X + 1) for _ in range(3)]

for v in range(3):
    for a, c in foods[v]:
        # Process in reverse to avoid using same item multiple times
        for cal in range(X, c - 1, -1):
            dp[v][cal] = max(dp[v][cal], dp[v][cal - c] + a)
    # Fill in values for lower calories (monotonic)
    for cal in range(X):
        dp[v][cal + 1] = max(dp[v][cal + 1], dp[v][cal])

# Try all possible calorie allocations
max_min_vitamin = 0

for c1 in range(X + 1):
    for c2 in range(X + 1 - c1):
        c3 = X - c1 - c2
        min_vitamin = min(dp[0][c1], dp[1][c2], dp[2][c3])
        max_min_vitamin = max(max_min_vitamin, min_vitamin)

print(max_min_vitamin)
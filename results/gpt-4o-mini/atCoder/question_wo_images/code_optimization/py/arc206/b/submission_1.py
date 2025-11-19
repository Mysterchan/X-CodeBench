n = int(input())
P = list(map(int, input().split()))
C = list(map(int, input().split()))

# Array to store the colors grouped by their value indices
color_buckets = [[] for _ in range(n + 1)]

# Store the colors based on the position of sizes in P
for i in range(n):
    color_buckets[P[i]].append(C[i])

total_cost = sum(C)
ans = 0

# Iterate over the color buckets to calculate the cost to rearrange
for colors in color_buckets[1:]:
    if colors:
        # Use a dynamic programming approach to find the longest increasing subsequence of colors
        dp = [1] * len(colors)
        for j in range(len(colors)):
            for k in range(j):
                if colors[j] > colors[k]:
                    dp[j] = max(dp[j], dp[k] + 1)
        # Calculate the overall answer by accumulating costs
        ans += max(dp)

# The answer is the total cost minus the maximum number of swaps we can perform
print(total_cost - ans)
def count_routes(test_cases):
    MOD = 998244353
    results = []

    for n, m, d, grid in test_cases:
        holds = [[[] for _ in range(m)] for _ in range(n)]
        
        # Collect the hold positions
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 'X':
                    holds[i][j].append((i, j))
        
        # dp to count routes from the bottom to the top
        dp = [[0] * m for _ in range(n)]
        
        # Initialize base case: the last row
        for j in range(m):
            if holds[n - 1][j]:
                dp[n - 1][j] = 1
        
        # Iterate from the second last row to the top
        for i in range(n - 2, -1, -1):
            for j in range(m):
                if holds[i][j]:
                    for x in range(m):
                        if holds[i + 1][x]:  # the next row
                            # Check distance constraint
                            if (i + 1 - i) ** 2 + (j - x) ** 2 <= d ** 2:
                                dp[i][j] = (dp[i][j] + dp[i + 1][x]) % MOD
        
        # Total valid routes from the top row (1) to the last row (n)
        total_routes = 0
        for j in range(m):
            if holds[0][j]:
                total_routes = (total_routes + dp[0][j]) % MOD
        
        results.append(total_routes)
    
    return results

# Input handling
import sys
input = sys.stdin.read

data = input().splitlines()
index = 0
t = int(data[index])
index += 1
test_cases = []

for _ in range(t):
    n, m, d = map(int, data[index].split())
    index += 1
    grid = [data[index + i] for i in range(n)]
    index += n
    test_cases.append((n, m, d, grid))

# Calculate and print result
results = count_routes(test_cases)
for result in results:
    print(result)
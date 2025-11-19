import sys
import math
from collections import defaultdict

MOD = 998244353

def count_routes(n, m, d, holds):
    # Build the list of holds in each row
    holds_per_row = []
    for i in range(n):
        row_holds = []
        for j in range(m):
            if holds[i][j] == 'X':
                row_holds.append(j)
        holds_per_row.append(row_holds)
        
    # Dynamic programming table
    dp = [defaultdict(int) for _ in range(n)]
    
    # Initialize the bottom level
    for j in holds_per_row[n-1]:
        dp[n-1][j] += 1

    # Process from the bottom up
    for i in range(n-2, -1, -1):
        for j in holds_per_row[i]:
            for k in holds_per_row[i+1]:
                if math.sqrt((i+1 - i) ** 2 + (k - j) ** 2) <= d:
                    dp[i][j] = (dp[i][j] + dp[i+1][k]) % MOD

    # Sum up all routes starting from the top row
    total_routes = sum(dp[0][j] for j in holds_per_row[0]) % MOD
    return total_routes

def main():
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        n, m, d = map(int, data[index].split())
        index += 1
        holds = [data[index + i] for i in range(n)]
        index += n
        results.append(count_routes(n, m, d, holds))

    sys.stdout.write("\n".join(map(str, results)) + "\n")

if __name__ == "__main__":
    main()
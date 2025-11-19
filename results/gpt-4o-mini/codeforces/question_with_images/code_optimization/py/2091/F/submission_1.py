from sys import stdin, stdout
import math

MOD = 998244353

def solve():
    n, m, d = map(int, stdin.readline().split())
    grid = [stdin.readline().strip() for _ in range(n)]
    
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the last row
    for j in range(m):
        if grid[n-1][j] == 'X':
            dp[n-1][j] = 1

    # Process from bottom to top
    for i in range(n-2, -1, -1):
        for j in range(m):
            if grid[i][j] == 'X':
                # Calculate the range of reachable holds in the next row
                for k in range(max(0, j - d), min(m, j + d + 1)):
                    if grid[i + 1][k] == 'X':
                        dp[i][j] = (dp[i][j] + dp[i + 1][k]) % MOD

    # Count valid routes from the top row
    result = 0
    for j in range(m):
        if grid[0][j] == 'X':
            result = (result + dp[0][j]) % MOD

    stdout.write(f"{result}\n")

def main():
    t = int(stdin.readline())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
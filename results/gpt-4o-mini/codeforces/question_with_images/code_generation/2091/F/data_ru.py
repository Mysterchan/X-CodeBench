MOD = 998244353

def count_routes(n, m, d, grid):
    # Collect all grips by level
    grips = []
    for i in range(n):
        level_grips = []
        for j in range(m):
            if grid[i][j] == 'X':
                level_grips.append(j)
        grips.append(level_grips)

    # Dynamic programming array
    dp = [[0] * m for _ in range(n)]
    
    # Initialize bottom level
    if not grips[n-1]:
        return 0
    for j in grips[n-1]:
        dp[n-1][j] = 1

    # Dynamic programming from bottom to top
    for i in range(n - 2, -1, -1):
        if not grips[i]:
            continue
        for j in grips[i]:
            # Now we need to find all grips in the level below we can reach
            for k in grips[i + 1]:  # grips on the next level
                if abs(j - k) <= d:
                    dp[i][j] = (dp[i][j] + dp[i + 1][k]) % MOD

    # Count valid routes from the top level
    result = 0
    for j in grips[0]:
        result = (result + dp[0][j]) % MOD
    
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, m, d = map(int, data[index].split())
        index += 1
        grid = [data[i] for i in range(index, index + n)]
        index += n
        results.append(count_routes(n, m, d, grid))
    
    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
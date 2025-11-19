def count_paths(n, m, d, grid):
    from collections import defaultdict
    import math

    MOD = 998244353

    # Find all grip points
    grips = [ [(j, i) for j in range(m) if grid[i][j] == 'X'] for i in range(n) ]

    # Early exit if the first row has no grips
    if not grips[-1]: 
        return 0

    # Dynamic programming dictionaries
    dp = [defaultdict(int) for _ in range(n)]

    # Initialize the base case (last row)
    for j1 in grips[-1]:
        dp[-1][j1] += 1

    # Process each row from bottom to top
    for i in range(n-2, -1, -1):
        if not grips[i]: 
            continue
        
        for j1 in grips[i+1]:
            # Check each pair of grips in current row and next row
            for x1, y1 in grips[i]:
                # Calculate the Euclidean distance
                if (x1 - j1[0]) ** 2 + (i - (i + 1)) ** 2 <= d ** 2:
                    dp[i][(x1, i)] += dp[i + 1][j1]
                    dp[i][(x1, i)] %= MOD

        if i > 0:
            for j1 in grips[i]:
                for j2 in grips[i-1]:
                    if (j1[0] - j2[0]) ** 2 + 1 <= d ** 2:
                        dp[i-1][j2] += dp[i][j1]
                        dp[i-1][j2] %= MOD

    # Sum counts from the first row (head)
    return sum(dp[0].values()) % MOD

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    t = int(data[0])
    index = 1
    results = []
    
    for _ in range(t):
        n, m, d = map(int, data[index].split())
        index += 1
        grid = [data[index + i] for i in range(n)]
        index += n
        
        result = count_paths(n, m, d, grid)
        results.append(result)

    print('\n'.join(map(str, results)))

if __name__ == "__main__":
    main()
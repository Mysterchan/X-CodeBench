def main():
    import sys
    sys.setrecursionlimit(10**7)
    N, K = map(int, sys.stdin.readline().split())

    # The path length is 2N-2 moves: N-1 downs (D) and N-1 rights (R)
    # We want to find the K-th path in the order defined by the problem:
    # At each step, if both down and right moves are possible,
    # choose the one whose destination cell has been visited fewer times in previous exercises.
    # If counts are equal, choose down.

    # The problem reduces to finding the K-th path in a special order.
    # The order is defined by the number of visits to the destination cells.
    # The visits count for each cell before the K-th exercise is the number of previous exercises that passed through it.

    # The key insight:
    # The number of times a cell (i,j) is visited before the K-th exercise is the number of paths among the first K-1 exercises that passed through (i,j).
    # Since the path always starts at (1,1) and ends at (N,N), and moves only down or right,
    # the number of paths passing through (i,j) is the number of paths from (1,1) to (i,j) times the number of paths from (i,j) to (N,N).
    # But here, the order of paths is defined by the rule of choosing moves based on visit counts.

    # The problem is equivalent to enumerating all paths from (1,1) to (N,N) with N-1 downs and N-1 rights,
    # sorted by the lex order defined by the rule:
    # At each step, if both moves possible, choose the one with fewer visits (i.e. fewer previous paths passing through that cell).
    # If equal, choose down.

    # This ordering corresponds to the lexicographically smallest path with respect to a custom order:
    # At each step, the "weight" of choosing down or right depends on the number of paths passing through the next cell.

    # We can precompute the number of paths from each cell to (N,N):
    # dp[i][j] = number of paths from (i,j) to (N,N)
    # dp[N][N] = 1
    # dp[i][j] = dp[i+1][j] + dp[i][j+1]

    # Then, at each step, we can decide whether to go down or right by comparing the number of paths through the down cell and right cell.
    # The number of previous visits to a cell before the K-th exercise is the number of paths before K that passed through it.
    # So the number of visits to the down cell is the number of paths before K that pass through it.
    # Similarly for the right cell.

    # Since the paths are enumerated in this order, the number of paths before K that pass through a cell is the count of paths before K that go through that cell.
    # So we can use dp to decide which move to take at each step.

    # We want to find the K-th path in this order.
    # At each step:
    # - If only down is possible, go down.
    # - If only right is possible, go right.
    # - If both possible:
    #   - Let down_count = dp[i+1][j]
    #   - Let right_count = dp[i][j+1]
    #   - If K <= down_count, go down
    #   - Else, K -= down_count, go right

    # This works because the paths are ordered so that all paths starting with down come first,
    # then all paths starting with right.

    # Precompute dp:
    dp = [[0]*(N+2) for _ in range(N+2)]
    dp[N][N] = 1
    for i in range(N, 0, -1):
        for j in range(N, 0, -1):
            if i == N and j == N:
                continue
            dp[i][j] = 0
            if i+1 <= N:
                dp[i][j] += dp[i+1][j]
            if j+1 <= N:
                dp[i][j] += dp[i][j+1]

    # Construct the path
    i, j = 1, 1
    path = []
    for _ in range(2*N - 2):
        if i == N:
            # can only go right
            path.append('R')
            j += 1
        elif j == N:
            # can only go down
            path.append('D')
            i += 1
        else:
            down_count = dp[i+1][j]
            if K <= down_count:
                path.append('D')
                i += 1
            else:
                K -= down_count
                path.append('R')
                j += 1

    print(''.join(path))


if __name__ == "__main__":
    main()
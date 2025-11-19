N, K = map(int, input().split())

# The path is determined by the number of visits to each cell before the K-th exercise.
# Each exercise corresponds to a path from (0,0) to (N-1,N-1) with exactly (N-1) downs and (N-1) rights.
# The order of moves is decided by comparing visit counts of the next down and right cells.
# The visit count of a cell (i,j) before the K-th exercise is the number of previous exercises that passed through it.
# 
# Key insight:
# The visit count of a cell (i,j) is the number of paths among the first K-1 exercises that pass through (i,j).
# The number of paths passing through (i,j) is the number of ways to reach (i,j) from (0,0) times the number of ways to reach (N-1,N-1) from (i,j).
# 
# Since the moves are always down or right, the number of paths from (0,0) to (i,j) is C(i+j, i).
# The number of paths from (i,j) to (N-1,N-1) is C(2N-2 - (i+j), N-1 - i).
# 
# The total number of paths is C(2N-2, N-1).
# The K-th path in the order defined by the problem corresponds to the K-th path in the lex order defined by the visit counts.
# 
# We can reconstruct the K-th path by:
# At each step, decide whether to go down or right by comparing the number of paths starting with down move.
# If the number of paths starting with down is >= K, go down.
# Else, subtract that number from K and go right.
# 
# This approach is efficient and works for large K (up to 10^18).

from math import comb

ans = []
i = j = 0
while i < N-1 or j < N-1:
    if i == N-1:
        ans.append('R')
        j += 1
    elif j == N-1:
        ans.append('D')
        i += 1
    else:
        # Number of paths if we go down next
        down_paths = comb((N-1 - i -1) + (N-1 - j), N-1 - i -1)
        if down_paths >= K:
            ans.append('D')
            i += 1
        else:
            K -= down_paths
            ans.append('R')
            j += 1

print(''.join(ans))
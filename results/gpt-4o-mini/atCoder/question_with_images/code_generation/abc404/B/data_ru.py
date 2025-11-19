def rotate(grid):
    N = len(grid)
    return [''.join(grid[N - j - 1][i] for j in range(N)) for i in range(N)]

def count_differences(S, T):
    return sum(1 for i in range(len(S)) for j in range(len(S)) if S[i][j] != T[i][j])

def min_operations(N, S, T):
    min_ops = float('inf')
    
    for _ in range(4):  # Check for 0, 90, 180, and 270 degrees
        diff_count = count_differences(S, T)
        min_ops = min(min_ops, diff_count)
        S = rotate(S)  # Rotate S by 90 degrees
    
    return min_ops

import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
S = data[1:N + 1]
T = data[N + 1:2 * N + 1]

print(min_operations(N, S, T))
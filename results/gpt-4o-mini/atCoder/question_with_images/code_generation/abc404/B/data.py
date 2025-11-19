def rotate(grid):
    N = len(grid)
    return [['' for _ in range(N)] for _ in range(N)] \
           if N == 0 else [[grid[N - j - 1][i] for j in range(N)] for i in range(N)]

def count_differences(S, T):
    return sum(S[i][j] != T[i][j] for i in range(len(S)) for j in range(len(S)))

def min_operations(N, S, T):
    min_ops = float('inf')
    
    for _ in range(4):  # Check for 0, 90, 180, and 270 degrees
        diff_count = count_differences(S, T)
        min_ops = min(min_ops, diff_count)
        S = rotate(S)  # Rotate S 90 degrees clockwise
    
    return min_ops

# Read input
import sys
input = sys.stdin.read
data = input().splitlines()

N = int(data[0])
S = [list(data[i + 1]) for i in range(N)]
T = [list(data[i + 1 + N]) for i in range(N)]

# Get the result and print it
result = min_operations(N, S, T)
print(result)
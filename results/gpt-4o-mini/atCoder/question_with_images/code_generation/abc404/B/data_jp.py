def rotate(grid):
    N = len(grid)
    return [['#' if grid[N - j - 1][i] == '.' else '.' for j in range(N)] for i in range(N)]

def count_changes(S, T):
    return sum(S[i][j] != T[i][j] for i in range(len(S)) for j in range(len(S)))

def min_operations(N, S, T):
    min_ops = float('inf')
    
    for _ in range(4):
        changes = count_changes(S, T)
        min_ops = min(min_ops, changes)
        S = rotate(S)
    
    return min_ops

# Input reading
N = int(input().strip())
S = [list(input().strip()) for _ in range(N)]
T = [list(input().strip()) for _ in range(N)]

# Output the result
print(min_operations(N, S, T))
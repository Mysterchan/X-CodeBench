def rotate_90(grid):
    N = len(grid)
    # Rotate 90 degrees clockwise: (i,j) -> (j, N-1-i)
    return [''.join(grid[N - 1 - i][j] for i in range(N)) for j in range(N)]

def min_operations_to_match(S, T):
    N = len(S)
    min_ops = float('inf')
    current = S
    for rotation_count in range(4):
        # Count differences
        diff = 0
        for i in range(N):
            for j in range(N):
                if current[i][j] != T[i][j]:
                    diff += 1
        # Total operations = rotation_count + diff (flip each differing cell)
        ops = rotation_count + diff
        if ops < min_ops:
            min_ops = ops
        # Rotate for next iteration
        current = rotate_90(current)
    return min_ops

def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = [input().rstrip('\n') for _ in range(N)]
    T = [input().rstrip('\n') for _ in range(N)]
    print(min_operations_to_match(S, T))

if __name__ == "__main__":
    main()
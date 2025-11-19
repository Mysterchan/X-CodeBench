def rotate_90(grid):
    N = len(grid)
    return [''.join(grid[N - 1 - j][i] for j in range(N)) for i in range(N)]

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = [input().rstrip('\n') for _ in range(N)]
    T = [input().rstrip('\n') for _ in range(N)]

    min_ops = float('inf')
    current = S
    for rot in range(4):
        # Count differences
        diff = 0
        for i in range(N):
            for j in range(N):
                if current[i][j] != T[i][j]:
                    diff += 1
        # Operations = rotations + flips
        ops = rot + diff
        if ops < min_ops:
            min_ops = ops
        current = rotate_90(current)

    print(min_ops)

if __name__ == "__main__":
    main()
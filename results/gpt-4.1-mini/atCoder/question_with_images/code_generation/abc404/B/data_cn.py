def rotate_90(grid):
    N = len(grid)
    return [''.join(grid[N - 1 - j][i] for j in range(N)) for i in range(N)]

def min_operations(N, S, T):
    res = float('inf')
    current = S
    for r in range(4):
        diff = 0
        for i in range(N):
            for j in range(N):
                if current[i][j] != T[i][j]:
                    diff += 1
        # total operations = number of rotations + number of cell flips
        res = min(res, r + diff)
        current = rotate_90(current)
    return res

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    S = [input().rstrip('\n') for _ in range(N)]
    T = [input().rstrip('\n') for _ in range(N)]
    print(min_operations(N, S, T))
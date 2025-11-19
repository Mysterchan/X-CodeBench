def rotate_90(grid):
    N = len(grid)
    return [''.join(grid[N - 1 - j][i] for j in range(N)) for i in range(N)]

def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    S = [input().rstrip() for _ in range(N)]
    T = [input().rstrip() for _ in range(N)]

    ans = float('inf')
    current = S
    for _ in range(4):
        # 色が異なるマスの数を数える
        diff = 0
        for i in range(N):
            for j in range(N):
                if current[i][j] != T[i][j]:
                    diff += 1
        ans = min(ans, diff)
        current = rotate_90(current)

    print(ans)

if __name__ == "__main__":
    main()
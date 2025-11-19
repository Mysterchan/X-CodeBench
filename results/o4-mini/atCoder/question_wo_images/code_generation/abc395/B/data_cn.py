def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    for i in range(N):
        row = []
        # 对于每个单元格 (i, j)，计算它到四条边的最小距离 ring
        for j in range(N):
            ring = min(i, j, N - 1 - i, N - 1 - j)
            # 偶数环为黑色 (#)，奇数环为白色 (.)
            row.append('#' if ring % 2 == 0 else '.')
        print(''.join(row))

if __name__ == "__main__":
    main()
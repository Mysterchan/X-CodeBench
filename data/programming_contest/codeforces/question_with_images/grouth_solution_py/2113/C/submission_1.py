import sys

def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out_lines = []
    for _ in range(t):
        n = int(data[idx]); m = int(data[idx+1]); k = int(data[idx+2]); idx += 3
        grid = []
        for _r in range(n):
            s = data[idx].decode()
            idx += 1
            grid.append(s)

        arr = [[0] * m for _ in range(n)]
        ring_total = 0
        for i in range(n):
            row = grid[i]
            for j, ch in enumerate(row):
                if ch == 'g':
                    if (i - k >= 0) or (i + k < n) or (j - k >= 0) or (j + k < m):
                        arr[i][j] = 1
                        ring_total += 1

        ps = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                ps[i+1][j+1] = arr[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]

        def rect_sum(r1, c1, r2, c2):
            return ps[r2+1][c2+1] - ps[r1][c2+1] - ps[r2+1][c1] + ps[r1][c1]

        K = k - 1
        INF = 10**9
        min_bad = INF
        for i in range(n):
            row = grid[i]
            for j, ch in enumerate(row):
                if ch == '.':
                    if K >= 0:
                        r1 = 0 if i <= K else i - K
                        c1 = 0 if j <= K else j - K
                        r2 = n - 1 if i + K >= n - 1 else i + K
                        c2 = m - 1 if j + K >= m - 1 else j + K
                        bad = rect_sum(r1, c1, r2, c2)
                        if bad < min_bad:
                            min_bad = bad

        ans = ring_total - (min_bad if min_bad != INF else 0)
        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()

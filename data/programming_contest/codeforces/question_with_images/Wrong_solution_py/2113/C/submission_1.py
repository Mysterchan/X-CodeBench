import sys
from collections import deque

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    t = int(next(it))
    out_lines = []

    for _ in range(t):
        n = int(next(it))
        m = int(next(it))
        k = int(next(it))

        grid = [next(it).decode() for _ in range(n)]

        if k == 0:
            out_lines.append("0")
            continue

        gold_pos = []
        empty = [[False] * m for _ in range(n)]
        gold_present = [[False] * m for _ in range(n)]

        for i in range(n):
            row = grid[i]
            for j, ch in enumerate(row):
                if ch == 'g':
                    gold_pos.append((i, j))
                    gold_present[i][j] = True
                elif ch == '.':
                    empty[i][j] = True

        total_gold = len(gold_pos)
        if total_gold == 0:
            out_lines.append("0")
            continue

        ps = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            row_sum = 0
            gi = i - 1
            for j in range(1, m + 1):
                row_sum += 1 if gold_present[gi][j - 1] else 0
                ps[i][j] = ps[i - 1][j] + row_sum

        def rect_sum(r1: int, c1: int, r2: int, c2: int) -> int:
            return (
                ps[r2 + 1][c2 + 1]
                - ps[r1][c2 + 1]
                - ps[r2 + 1][c1]
                + ps[r1][c1]
            )

        radius_inner = k - 1
        inner = [[0] * m for _ in range(n)]

        if radius_inner >= 0:
            for i in range(n):
                for j in range(m):
                    r1 = i - radius_inner
                    r2 = i + radius_inner
                    c1 = j - radius_inner
                    c2 = j + radius_inner
                    if r1 < 0:
                        r1 = 0
                    if r2 >= n:
                        r2 = n - 1
                    if c1 < 0:
                        c1 = 0
                    if c2 >= m:
                        c2 = m - 1
                    inner[i][j] = rect_sum(r1, c1, r2, c2)

        q = deque()
        in_queue = [[False] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if empty[i][j] and inner[i][j] == 0:
                    q.append((i, j))
                    in_queue[i][j] = True

        ans = 0
        radius_outer = k

        while q:
            x, y = q.popleft()
            in_queue[x][y] = False

            if not empty[x][y] or inner[x][y] != 0:
                continue

            for dx in (-radius_outer, radius_outer):
                nx = x + dx
                if nx < 0 or nx >= n:
                    continue
                for dy in range(-radius_outer, radius_outer + 1):
                    ny = y + dy
                    if ny < 0 or ny >= m:
                        continue
                    if gold_present[nx][ny]:
                        gold_present[nx][ny] = False
                        ans += 1
                        r1 = nx - radius_inner
                        r2 = nx + radius_inner
                        c1 = ny - radius_inner
                        c2 = ny + radius_inner
                        if r1 < 0:
                            r1 = 0
                        if r2 >= n:
                            r2 = n - 1
                        if c1 < 0:
                            c1 = 0
                        if c2 >= m:
                            c2 = m - 1
                        for ii in range(r1, r2 + 1):
                            row_inner = inner[ii]
                            for jj in range(c1, c2 + 1):
                                row_inner[jj] -= 1
                                if row_inner[jj] == 0 and empty[ii][jj] and not in_queue[ii][jj]:
                                    q.append((ii, jj))
                                    in_queue[ii][jj] = True

            for dy in (-radius_outer, radius_outer):
                ny = y + dy
                if ny < 0 or ny >= m:
                    continue
                for dx in range(-radius_outer + 1, radius_outer):
                    nx = x + dx
                    if nx < 0 or nx >= n:
                        continue
                    if gold_present[nx][ny]:
                        gold_present[nx][ny] = False
                        ans += 1
                        r1 = nx - radius_inner
                        r2 = nx + radius_inner
                        c1 = ny - radius_inner
                        c2 = ny + radius_inner
                        if r1 < 0:
                            r1 = 0
                        if r2 >= n:
                            r2 = n - 1
                        if c1 < 0:
                            c1 = 0
                        if c2 >= m:
                            c2 = m - 1
                        for ii in range(r1, r2 + 1):
                            row_inner = inner[ii]
                            for jj in range(c1, c2 + 1):
                                row_inner[jj] -= 1
                                if row_inner[jj] == 0 and empty[ii][jj] and not in_queue[ii][jj]:
                                    q.append((ii, jj))
                                    in_queue[ii][jj] = True
            r1 = x - radius_outer
            r2 = x + radius_outer
            c1 = y - radius_outer
            c2 = y + radius_outer
            if r1 < 0:
                r1 = 0
            if r2 >= n:
                r2 = n - 1
            if c1 < 0:
                c1 = 0
            if c2 >= m:
                c2 = m - 1
            for i2 in range(r1, r2 + 1):
                row_empty = empty[i2]
                row_inner = inner[i2]
                for j2 in range(c1, c2 + 1):
                    if not row_empty[j2]:
                        row_empty[j2] = True
                        if row_inner[j2] == 0 and not in_queue[i2][j2]:
                            q.append((i2, j2))
                            in_queue[i2][j2] = True

        out_lines.append(str(ans))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()

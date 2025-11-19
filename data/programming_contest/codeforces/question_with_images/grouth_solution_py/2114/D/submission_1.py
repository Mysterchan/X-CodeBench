import sys

def solve() -> None:
    it = iter(sys.stdin.read().strip().split())
    t = int(next(it))
    out_lines = []

    INF = 10**20

    for _ in range(t):
        n = int(next(it))
        points = []
        xs = [0] * n
        ys = [0] * n
        for i in range(n):
            x = int(next(it))
            y = int(next(it))
            xs[i] = x
            ys[i] = y
            points.append((x, y))

        if n == 1:
            out_lines.append('1')
            continue

        xs_sorted = sorted(xs)
        ys_sorted = sorted(ys)

        min_x = xs_sorted[0]
        cnt_min_x = 0
        while cnt_min_x < n and xs_sorted[cnt_min_x] == min_x:
            cnt_min_x += 1
        second_min_x = xs_sorted[cnt_min_x] if cnt_min_x < n else None

        max_x = xs_sorted[-1]
        cnt_max_x = 0
        j = n - 1
        while j >= 0 and xs_sorted[j] == max_x:
            cnt_max_x += 1
            j -= 1
        second_max_x = xs_sorted[-cnt_max_x - 1] if cnt_max_x < n else None

        min_y = ys_sorted[0]
        cnt_min_y = 0
        while cnt_min_y < n and ys_sorted[cnt_min_y] == min_y:
            cnt_min_y += 1
        second_min_y = ys_sorted[cnt_min_y] if cnt_min_y < n else None

        max_y = ys_sorted[-1]
        cnt_max_y = 0
        j = n - 1
        while j >= 0 and ys_sorted[j] == max_y:
            cnt_max_y += 1
            j -= 1
        second_max_y = ys_sorted[-cnt_max_y - 1] if cnt_max_y < n else None

        width0 = max_x - min_x + 1
        height0 = max_y - min_y + 1
        answer = width0 * height0

        y_at_min_x = None
        y_at_max_x = None
        x_at_min_y = None
        x_at_max_y = None

        for x, y in points:
            if cnt_min_x == 1 and x == min_x:
                y_at_min_x = y
            if cnt_max_x == 1 and x == max_x:
                y_at_max_x = y
            if cnt_min_y == 1 and y == min_y:
                x_at_min_y = x
            if cnt_max_y == 1 and y == max_y:
                x_at_max_y = x

        def try_remove(change_min_x: bool, change_max_x: bool,
                       change_min_y: bool, change_max_y: bool) -> None:
            nonlocal answer

            new_min_x = min_x if not change_min_x else second_min_x
            new_max_x = max_x if not change_max_x else second_max_x
            new_min_y = min_y if not change_min_y else second_min_y
            new_max_y = max_y if not change_max_y else second_max_y

            width = new_max_x - new_min_x + 1
            height = new_max_y - new_min_y + 1
            area0 = width * height

            if area0 > n - 1:
                if area0 < answer:
                    answer = area0
            else:
                extra = min(width, height)
                cand = area0 + extra
                if cand < answer:
                    answer = cand

        if cnt_min_x == 1 and second_min_x is not None:
            try_remove(change_min_x=True, change_max_x=False,
                       change_min_y=(cnt_min_y == 1 and y_at_min_x == min_y),
                       change_max_y=(cnt_max_y == 1 and y_at_min_x == max_y))

        if cnt_max_x == 1 and second_max_x is not None:
            try_remove(change_min_x=False, change_max_x=True,
                       change_min_y=(cnt_min_y == 1 and y_at_max_x == min_y),
                       change_max_y=(cnt_max_y == 1 and y_at_max_x == max_y))

        if cnt_min_y == 1 and second_min_y is not None:
            try_remove(change_min_x=(cnt_min_x == 1 and x_at_min_y == min_x),
                       change_max_x=(cnt_max_x == 1 and x_at_min_y == max_x),
                       change_min_y=True, change_max_y=False)

        if cnt_max_y == 1 and second_max_y is not None:
            try_remove(change_min_x=(cnt_min_x == 1 and x_at_max_y == min_x),
                       change_max_x=(cnt_max_x == 1 and x_at_max_y == max_x),
                       change_min_y=False, change_max_y=True)

        out_lines.append(str(answer))

    sys.stdout.write("\n".join(out_lines))


if __name__ == "__main__":
    solve()

import sys

def main():
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index]); index += 1
        points = []
        xs = []
        ys = []
        for i in range(n):
            x = int(data[index]); y = int(data[index+1]); index += 2
            points.append((x, y))
            xs.append(x)
            ys.append(y)

        if n == 1:
            results.append("1")
            continue

        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        A0 = (max_x - min_x + 1) * (max_y - min_y + 1)

        freq_min_x = xs.count(min_x)
        freq_max_x = xs.count(max_x)
        freq_min_y = ys.count(min_y)
        freq_max_y = ys.count(max_y)

        distinct_x = sorted(set(xs))
        distinct_y = sorted(set(ys))

        if len(distinct_x) > 1:
            next_min_x = distinct_x[1]
            next_max_x = distinct_x[-2]
        else:
            next_min_x = distinct_x[0]
            next_max_x = distinct_x[0]

        if len(distinct_y) > 1:
            next_min_y = distinct_y[1]
            next_max_y = distinct_y[-2]
        else:
            next_min_y = distinct_y[0]
            next_max_y = distinct_y[0]

        best_after_move = 10**40
        for (x, y) in points:
            if x == min_x:
                if freq_min_x == 1:
                    cand_min_x = next_min_x
                else:
                    cand_min_x = min_x
            else:
                cand_min_x = min_x

            if x == max_x:
                if freq_max_x == 1:
                    cand_max_x = next_max_x
                else:
                    cand_max_x = max_x
            else:
                cand_max_x = max_x

            if y == min_y:
                if freq_min_y == 1:
                    cand_min_y = next_min_y
                else:
                    cand_min_y = min_y
            else:
                cand_min_y = min_y

            if y == max_y:
                if freq_max_y == 1:
                    cand_max_y = next_max_y
                else:
                    cand_max_y = max_y
            else:
                cand_max_y = max_y

            width = cand_max_x - cand_min_x + 1
            height = cand_max_y - cand_min_y + 1
            total_cells = width * height
            if total_cells == n - 1:
                area_i = total_cells + min(width, height)
            else:
                area_i = total_cells

            if area_i < best_after_move:
                best_after_move = area_i

        ans = min(A0, best_after_move)
        results.append(str(ans))

    print("\n".join(results))

if __name__ == "__main__":
    main()

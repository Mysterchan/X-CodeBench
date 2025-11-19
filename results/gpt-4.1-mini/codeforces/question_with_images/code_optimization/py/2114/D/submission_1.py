import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    results = []
    for _ in range(t):
        n = int(input())
        xs = [0]*n
        ys = [0]*n
        for i in range(n):
            x, y = map(int, input().split())
            xs[i] = x
            ys[i] = y

        if n == 1:
            results.append("1")
            continue

        min_x = min(xs)
        max_x = max(xs)
        min_y = min(ys)
        max_y = max(ys)

        A0 = (max_x - min_x + 1) * (max_y - min_y + 1)

        # Count frequencies of min_x, max_x, min_y, max_y
        freq_min_x = freq_max_x = freq_min_y = freq_max_y = 0
        for i in range(n):
            if xs[i] == min_x:
                freq_min_x += 1
            if xs[i] == max_x:
                freq_max_x += 1
            if ys[i] == min_y:
                freq_min_y += 1
            if ys[i] == max_y:
                freq_max_y += 1

        distinct_x = sorted(set(xs))
        distinct_y = sorted(set(ys))

        # Precompute next min and max for x
        if len(distinct_x) > 1:
            next_min_x = distinct_x[1]
            next_max_x = distinct_x[-2]
        else:
            next_min_x = distinct_x[0]
            next_max_x = distinct_x[0]

        # Precompute next min and max for y
        if len(distinct_y) > 1:
            next_min_y = distinct_y[1]
            next_max_y = distinct_y[-2]
        else:
            next_min_y = distinct_y[0]
            next_max_y = distinct_y[0]

        best_after_move = 10**40
        for i in range(n):
            x = xs[i]
            y = ys[i]

            # Adjust min_x
            if x == min_x:
                cand_min_x = next_min_x if freq_min_x == 1 else min_x
            else:
                cand_min_x = min_x

            # Adjust max_x
            if x == max_x:
                cand_max_x = next_max_x if freq_max_x == 1 else max_x
            else:
                cand_max_x = max_x

            # Adjust min_y
            if y == min_y:
                cand_min_y = next_min_y if freq_min_y == 1 else min_y
            else:
                cand_min_y = min_y

            # Adjust max_y
            if y == max_y:
                cand_max_y = next_max_y if freq_max_y == 1 else max_y
            else:
                cand_max_y = max_y

            width = cand_max_x - cand_min_x + 1
            height = cand_max_y - cand_min_y + 1
            total_cells = width * height

            # If rectangle covers exactly n-1 monsters, add min(width, height)
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
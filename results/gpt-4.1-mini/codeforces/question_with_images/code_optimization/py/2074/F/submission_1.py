import sys

def main():
    input = sys.stdin.readline
    t = int(input())
    results = []
    for _ in range(t):
        l1, r1, l2, r2 = map(int, input().split())
        w = r1 - l1
        h = r2 - l2

        def count_nodes(x0, x1, y0, y1):
            w = x1 - x0
            h = y1 - y0
            if w <= 0 or h <= 0:
                return 0
            if w == h and (w & (w - 1)) == 0 and x0 % w == 0 and y0 % w == 0:
                return 1
            s = 1 << (min(w, h).bit_length() - 1)
            res = 0
            # Calculate next division points aligned to s
            next_x = ((x0 + s) // s) * s
            next_y = ((y0 + s) // s) * s

            # Clamp next_x and next_y to not exceed x1 and y1
            if next_x > x1:
                next_x = None
            if next_y > y1:
                next_y = None

            if next_x is not None and next_y is not None:
                res += count_nodes(x0, next_x, y0, next_y)
                res += count_nodes(x0, next_x, next_y, y1)
                res += count_nodes(next_x, x1, y0, next_y)
                res += count_nodes(next_x, x1, next_y, y1)
            elif next_x is not None:
                res += count_nodes(x0, next_x, y0, y1)
                res += count_nodes(next_x, x1, y0, y1)
            elif next_y is not None:
                res += count_nodes(x0, x1, y0, next_y)
                res += count_nodes(x0, x1, next_y, y1)
            else:
                # This case happens only if w or h == 0, but handled above
                res += w * h
            return res

        results.append(str(count_nodes(l1, r1, l2, r2)))
    print("\n".join(results))

if __name__ == "__main__":
    main()
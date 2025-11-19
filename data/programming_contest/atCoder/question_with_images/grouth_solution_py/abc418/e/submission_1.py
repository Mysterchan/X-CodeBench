import math
import sys
from collections import Counter, defaultdict

def main():
    input = sys.stdin.readline
    N = int(input())
    pts = [tuple(map(int, input().split())) for _ in range(N)]

    cnt_dir = Counter()
    cnt_dir_len = Counter()

    for i in range(N):
        x1, y1 = pts[i]
        for j in range(i + 1, N):
            x2, y2 = pts[j]
            dx = x2 - x1
            dy = y2 - y1

            if dx == 0:
                dir_key = ("inf", 0)
            elif dy == 0:
                dir_key = (0, "inf")
            else:
                g = math.gcd(dx, dy)
                dx0 = dx // g
                dy0 = dy // g

                if dy0 < 0:
                    dx0 = -dx0
                    dy0 = -dy0
                dir_key = (dy0, dx0)

            length_sq = dx * dx + dy * dy

            cnt_dir[dir_key] += 1
            cnt_dir_len[(dir_key, length_sq)] += 1

    total_parallel_pairs = 0
    for v in cnt_dir.values():

        total_parallel_pairs += v * (v - 1) // 2

    subtract_for_parallelograms = 0
    for v in cnt_dir_len.values():
        subtract_for_parallelograms += v * (v - 1) // 2

    result = total_parallel_pairs - subtract_for_parallelograms // 2

    print(result)

if __name__ == "__main__":
    main()
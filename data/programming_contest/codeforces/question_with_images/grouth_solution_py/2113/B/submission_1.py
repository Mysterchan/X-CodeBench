import sys

def solve() -> None:
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        w, h, a, b = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())

        dx = abs(x1 - x2)
        dy = abs(y1 - y2)

        if dx < a and dy < b:
            print("No")
            continue

        if dy < b:
            if dx >= a and (dx - a) % a == 0:
                print("Yes")
            else:
                print("No")
            continue

        if dx < a:
            if dy >= b and (dy - b) % b == 0:
                print("Yes")
            else:
                print("No")
            continue

        gap_x = dx - a
        gap_y = dy - b
        if gap_x % a == 0 or gap_y % b == 0:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    solve()

import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        l1, r1, l2, r2 = map(int, input().split())
        width = r1 - l1
        height = r2 - l2

        # Find the smallest power of two >= width
        pw = 1
        while pw < width:
            pw <<= 1
        # Find the smallest power of two >= height
        ph = 1
        while ph < height:
            ph <<= 1

        # The minimal number of nodes is the product of these two powers of two
        print(pw * ph)

if __name__ == "__main__":
    solve()
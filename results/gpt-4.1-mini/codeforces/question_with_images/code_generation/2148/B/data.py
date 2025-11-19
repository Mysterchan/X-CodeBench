import sys
import bisect

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    # Count how many horizontal lasers are strictly between 0 and y
    # We want to count how many a_i satisfy 0 < a_i < y
    # Since a is sorted and all a_i satisfy 0 < a_i < y, all are valid
    # But we need to count how many are strictly less than y (which they all are)
    # So count of horizontal lasers crossed is number of a_i < y
    # Since a_i < y guaranteed, count is n

    # Similarly for vertical lasers, count how many b_i satisfy 0 < b_i < x
    # All b_i satisfy 0 < b_i < x, so count is m

    # But we must consider that we can choose a path that crosses some lasers and avoids others.
    # The minimal number of crossings is the minimal number of lasers that must be crossed.
    # Since we start at (0,0) and end at (x,y), any path must cross all lasers that lie between 0 and x or 0 and y.
    # But we can avoid some lasers by going around them if possible.

    # Actually, the problem states that the lasers span the entire width or height:
    # Horizontal lasers: from (0, a_i) to (x, a_i)
    # Vertical lasers: from (b_i, 0) to (b_i, y)
    # So to get from (0,0) to (x,y), we must cross all horizontal lasers with a_i in (0,y)
    # and all vertical lasers with b_i in (0,x).

    # So the minimal crossings is the number of horizontal lasers + number of vertical lasers.

    # But the problem's example shows that the minimal crossings is 2 when n=m=1, x=y=2, a=[1], b=[1].
    # So minimal crossings = n + m.

    # Wait, the problem states that crossing an intersection counts as two crossings.
    # But we can avoid crossing at the intersection by going around it.
    # So the minimal crossings is n + m.

    # So the answer is n + m.

    # However, the problem constraints say a_i < y and b_i < x, so all lasers are strictly inside the plane.

    # So minimal crossings = n + m.

    # Let's output n + m.

    print(n + m)
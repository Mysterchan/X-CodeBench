import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    arr = list(map(int, input().split()))
    dis = ((px - qx) ** 2 + (py - qy) ** 2) ** 0.5
    s = sum(arr)
    max_a = max(arr)
    # Check triangle inequality conditions:
    # 1) The distance between start and end must be <= sum of all moves
    # 2) The largest move must be <= sum of the rest moves + dis
    if dis <= s and max_a <= s - max_a + dis:
        print("Yes")
    else:
        print("No")
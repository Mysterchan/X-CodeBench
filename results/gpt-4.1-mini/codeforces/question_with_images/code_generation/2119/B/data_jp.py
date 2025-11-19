import sys
import math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    px, py, qx, qy = map(int, input().split())
    a = list(map(int, input().split()))

    dist = math.sqrt((qx - px) ** 2 + (qy - py) ** 2)
    s = sum(a)
    max_a = max(a)

    # 到達可能条件：
    # 1. 総移動距離の合計が目的地までの距離以上であること
    # 2. 三角不等式より、最大の移動距離が残りの移動距離の合計以下であること
    #    そうでないと、最後に目的地に到達できない
    if dist <= s and max_a <= s - max_a:
        print("Yes")
    else:
        print("No")
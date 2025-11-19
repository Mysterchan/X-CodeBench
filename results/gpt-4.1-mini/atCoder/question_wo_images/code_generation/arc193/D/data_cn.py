import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    B = input().strip()

    # 收集A中棋子位置
    posA = [i for i, ch in enumerate(A) if ch == '1']
    # 收集B中需要棋子的位置
    posB = [i for i, ch in enumerate(B) if ch == '1']

    # 若棋子數量不等，必定無法達成
    if len(posA) != len(posB):
        print(-1)
        continue

    # 對應位置配對，計算最大距離差
    max_dist = 0
    for a, b in zip(posA, posB):
        dist = abs(a - b)
        if dist > max_dist:
            max_dist = dist

    print(max_dist)
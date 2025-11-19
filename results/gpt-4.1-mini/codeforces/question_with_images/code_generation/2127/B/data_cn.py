import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    s = input().strip()
    x -= 1  # 0-based index

    # 找出Hamid左邊最近的牆壁位置（若無則為-1）
    left_wall = -1
    for i in range(x - 1, -1, -1):
        if s[i] == '#':
            left_wall = i
            break

    # 找出Hamid右邊最近的牆壁位置（若無則為n）
    right_wall = n
    for i in range(x + 1, n):
        if s[i] == '#':
            right_wall = i
            break

    # Mani想最大化逃脫天數，Hamid想最小化
    # 逃脫天數 = 1 + min(距離左牆, 距離右牆)
    # 若某側無牆，距離為該側距離到邊界（Hamid可直接逃脫，天數=1）
    # 但 Mani 每天只能建一堵牆，且不能在Hamid所在格子建牆
    # 因此，逃脫天數 = 1 + min(距離左牆, 距離右牆)
    # 若某側無牆，距離為距離邊界（Hamid可直接逃脫，天數=1）

    dist_left = x - left_wall if left_wall != -1 else x + 1
    dist_right = right_wall - x if right_wall != n else n - x

    # 答案為 1 + min(dist_left, dist_right) - 1 = min(dist_left, dist_right)
    # 因為第一天Hamid可以直接逃脫(0天)，但題目要求天數從1開始計算
    # 實際上，逃脫天數 = min(dist_left, dist_right)
    # 但根據題意，第一天 Mani 先建牆，然後 Hamid 移動或逃脫
    # 如果 Hamid 旁邊沒有牆，Hamid當天就逃脫，天數=1
    # 如果有牆，Hamid需摧毀牆壁並移動，天數會增加

    # 綜合以上，答案為 min(dist_left, dist_right)

    print(min(dist_left, dist_right))
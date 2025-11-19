import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    grid = [input().rstrip() for __ in range(n)]

    # 金の位置を記録
    gold = [[0]*m for __ in range(n)]
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'g':
                gold[i][j] = 1

    # 金の2D累積和を作成
    # sum_gold[i+1][j+1] = gridの(0,0)から(i,j)までの金の数
    sum_gold = [[0]*(m+1) for __ in range(n+1)]
    for i in range(n):
        row_sum = 0
        for j in range(m):
            row_sum += gold[i][j]
            sum_gold[i+1][j+1] = sum_gold[i][j+1] + row_sum

    def get_sum(x1, y1, x2, y2):
        # (x1,y1)から(x2,y2)までの矩形内の金の数を返す
        # 範囲外は0扱い
        if x2 < x1 or y2 < y1:
            return 0
        x1 = max(0, x1)
        y1 = max(0, y1)
        x2 = min(n-1, x2)
        y2 = min(m-1, y2)
        if x1 > x2 or y1 > y2:
            return 0
        return sum_gold[x2+1][y2+1] - sum_gold[x1][y2+1] - sum_gold[x2+1][y1] + sum_gold[x1][y1]

    max_gold = 0
    # 空セルで爆発可能な場所を探す
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '.':
                continue
            # 爆発範囲の境界座標
            top = i - k
            bottom = i + k
            left = j - k
            right = j + k

            # 境界の金の数
            # 境界は4辺の和から4隅の重複を引く
            # 上辺
            top_gold = get_sum(top, left, top, right)
            # 下辺
            bottom_gold = get_sum(bottom, left, bottom, right)
            # 左辺
            left_gold = get_sum(top+1, left, bottom-1, left)
            # 右辺
            right_gold = get_sum(top+1, right, bottom-1, right)

            boundary_gold = top_gold + bottom_gold + left_gold + right_gold

            # 内部の金は消えるので無視（問題文より）
            # 最大値更新
            if boundary_gold > max_gold:
                max_gold = boundary_gold

    print(max_gold)
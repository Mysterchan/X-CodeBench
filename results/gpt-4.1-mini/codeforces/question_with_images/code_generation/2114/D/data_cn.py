import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    xs = []
    ys = []
    for __ in range(n):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    # 不移動時的矩形面積
    base_area = (max_x - min_x + 1) * (max_y - min_y + 1)
    res = base_area

    # 嘗試移動一隻怪物，將其放置在邊界內縮一格的位置，嘗試縮小矩形
    # 移動怪物後，矩形邊界可能縮小，嘗試四種邊界縮小的可能：
    # 1. 將最大x縮小一格（即移動最大x的怪物）
    # 2. 將最小x增大一格（即移動最小x的怪物）
    # 3. 將最大y縮小一格（即移動最大y的怪物）
    # 4. 將最小y增大一格（即移動最小y的怪物）
    # 但要確保縮小後邊界仍包含所有其他怪物

    # 為了判斷縮小邊界後是否仍包含所有怪物，先找出次大/次小的x和y
    xs_sorted = sorted(xs)
    ys_sorted = sorted(ys)

    # 次小和次大
    if n > 1:
        second_min_x = xs_sorted[1]
        second_max_x = xs_sorted[-2]
        second_min_y = ys_sorted[1]
        second_max_y = ys_sorted[-2]
    else:
        # 只有一隻怪物，移動後面積為1
        print(1)
        continue

    # 移動最大x的怪物，將max_x縮小到second_max_x
    # 新矩形邊界: [min_x, second_max_x] x [min_y, max_y]
    area = (second_max_x - min_x + 1) * (max_y - min_y + 1)
    if area < res:
        res = area

    # 移動最小x的怪物，將min_x增大到second_min_x
    # 新矩形邊界: [second_min_x, max_x] x [min_y, max_y]
    area = (max_x - second_min_x + 1) * (max_y - min_y + 1)
    if area < res:
        res = area

    # 移動最大y的怪物，將max_y縮小到second_max_y
    # 新矩形邊界: [min_x, max_x] x [min_y, second_max_y]
    area = (max_x - min_x + 1) * (second_max_y - min_y + 1)
    if area < res:
        res = area

    # 移動最小y的怪物，將min_y增大到second_min_y
    # 新矩形邊界: [min_x, max_x] x [second_min_y, max_y]
    area = (max_x - min_x + 1) * (max_y - second_min_y + 1)
    if area < res:
        res = area

    print(res)
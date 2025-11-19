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

    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)

    # 初期の長方形のコスト（移動なし）
    base_cost = (max_x - min_x + 1) * (max_y - min_y + 1)

    # 移動を1回だけ行い、長方形のコストを最小化することを考える
    # 移動は1匹のモンスターを任意の空セルに移動可能
    # つまり、1匹のモンスターを使って長方形の範囲を狭めることができる

    # 可能な最小コストは、(max_x - min_x + 1 - dx) * (max_y - min_y + 1 - dy)
    # ただし dx, dy は0か1で、移動で端を縮められるかどうかを判定する

    # 端のモンスターの位置を調べて、端を縮められるか判定する
    # 端を縮めるとは、例えば最小xのモンスターが複数いる場合、
    # そのうち1匹を移動させて最小xを1つ増やせるかどうか

    from collections import Counter

    cx = Counter(xs)
    cy = Counter(ys)

    # 端のモンスターの数
    min_x_count = cx[min_x]
    max_x_count = cx[max_x]
    min_y_count = cy[min_y]
    max_y_count = cy[max_y]

    # 端を縮められるか判定
    # 端のモンスターが1匹だけなら、そのモンスターを移動させて端を縮められる
    # 端のモンスターが複数なら、移動しても端は縮まらない

    can_shrink_x_min = (min_x_count == 1)
    can_shrink_x_max = (max_x_count == 1)
    can_shrink_y_min = (min_y_count == 1)
    can_shrink_y_max = (max_y_count == 1)

    # 端を縮めるパターンを全探索（最大4つの端のうちどれを縮めるか）
    # ただし移動は1回だけなので、縮める端は最大1つか2つ（縦横両方）まで
    # 2つ以上の端を縮める場合は、縮める端が同じモンスターで可能かを考慮する必要があるが、
    # 1回の移動で端を2つ縮めることは可能（例えば最小xかつ最小yのモンスターを移動させれば両方縮まる）

    # 端を縮める組み合わせは以下の通り（0～2端まで）
    # 0端縮め
    # 1端縮め: min_x, max_x, min_y, max_y
    # 2端縮め: (min_x & min_y), (min_x & max_y), (max_x & min_y), (max_x & max_y)

    # 端を縮める条件を満たすか判定し、縮められる場合はコストを計算

    candidates = []

    # 0端縮め
    candidates.append(base_cost)

    # 1端縮め
    if can_shrink_x_min:
        cost = (max_x - (min_x + 1) + 1) * (max_y - min_y + 1)
        candidates.append(cost)
    if can_shrink_x_max:
        cost = ((max_x - 1) - min_x + 1) * (max_y - min_y + 1)
        candidates.append(cost)
    if can_shrink_y_min:
        cost = (max_x - min_x + 1) * (max_y - (min_y + 1) + 1)
        candidates.append(cost)
    if can_shrink_y_max:
        cost = (max_x - min_x + 1) * ((max_y - 1) - min_y + 1)
        candidates.append(cost)

    # 2端縮め
    # 2端縮めは、両方の端が1匹ずつなら可能か？
    # しかし1回の移動で2端縮めるには、そのモンスターが両方の端にいる必要がある
    # つまり、例えば min_x と min_y の端を縮めるには、
    # そのモンスターが (min_x, min_y) にいる必要がある

    # 端のモンスターの座標をセットで管理して判定
    pos_set = set(zip(xs, ys))

    # (min_x, min_y)
    if can_shrink_x_min and can_shrink_y_min and (min_x, min_y) in pos_set:
        cost = (max_x - (min_x + 1) + 1) * (max_y - (min_y + 1) + 1)
        candidates.append(cost)
    # (min_x, max_y)
    if can_shrink_x_min and can_shrink_y_max and (min_x, max_y) in pos_set:
        cost = (max_x - (min_x + 1) + 1) * ((max_y - 1) - min_y + 1)
        candidates.append(cost)
    # (max_x, min_y)
    if can_shrink_x_max and can_shrink_y_min and (max_x, min_y) in pos_set:
        cost = ((max_x - 1) - min_x + 1) * (max_y - (min_y + 1) + 1)
        candidates.append(cost)
    # (max_x, max_y)
    if can_shrink_x_max and can_shrink_y_max and (max_x, max_y) in pos_set:
        cost = ((max_x - 1) - min_x + 1) * ((max_y - 1) - min_y + 1)
        candidates.append(cost)

    print(min(candidates))
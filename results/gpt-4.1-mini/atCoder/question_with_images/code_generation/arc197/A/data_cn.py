import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    S = input().strip()

    # 计算S中已确定的D和R数量
    d_count = S.count('D')
    r_count = S.count('R')

    # 剩余的D和R数量
    d_remain = (H - 1) - d_count
    r_remain = (W - 1) - r_count

    # 构造两个路径：
    # path1: 将所有 '?' 替换为 'D'（尽可能多向下）
    # path2: 将所有 '?' 替换为 'R'（尽可能多向右）
    # 但要保证总数正确，先用已知的D和R，再用剩余的D和R填充

    # 先构造 path1: '?'优先替换为'D'，剩余替换为'R'
    path1 = []
    d_used = d_count
    r_used = r_count
    for c in S:
        if c == 'D':
            path1.append('D')
        elif c == 'R':
            path1.append('R')
        else:
            if d_used < H - 1:
                path1.append('D')
                d_used += 1
            else:
                path1.append('R')
                r_used += 1

    # 构造 path2: '?'优先替换为'R'，剩余替换为'D'
    path2 = []
    d_used = d_count
    r_used = r_count
    for c in S:
        if c == 'D':
            path2.append('D')
        elif c == 'R':
            path2.append('R')
        else:
            if r_used < W - 1:
                path2.append('R')
                r_used += 1
            else:
                path2.append('D')
                d_used += 1

    # 计算路径1的终点坐标
    # 起点为(1,1)
    # D向下+1，R向右+1
    d1 = path1.count('D')
    r1 = path1.count('R')
    # 终点坐标
    end1 = (1 + d1, 1 + r1)

    # 计算路径2的终点坐标
    d2 = path2.count('D')
    r2 = path2.count('R')
    end2 = (1 + d2, 1 + r2)

    # 计算两个路径的交集格子数
    # 路径上的格子数 = H + W - 1
    # 两条路径的交集格子数 = (min(d1,d2) + 1) + (min(r1,r2) + 1) - 1 = min(d1,d2) + min(r1,r2) + 1
    # 这里的+1是起点格子，-1是因为起点被重复计算
    # 但实际上，路径是从(1,1)开始，经过d个D和r个R，路径长度为H+W-1
    # 两路径交集是从起点开始，向下走min(d1,d2)步，向右走min(r1,r2)步的矩形路径上的格子数
    # 交集格子数 = (min(d1,d2) + min(r1,r2) + 1)

    inter = min(d1, d2) + min(r1, r2) + 1

    # 两条路径各自格子数
    len_path = H + W - 1

    # 最大黑格数 = 路径1格子数 + 路径2格子数 - 交集格子数
    ans = len_path + len_path - inter

    print(ans)
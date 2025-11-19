N, R, C = map(int, input().split())
S = input()

# 風向對應的座標變化 (r, c)
dir_map = {
    'N': (-1, 0),
    'W': (0, -1),
    'S': (1, 0),
    'E': (0, 1)
}

# 反向移動方向，因為我們要判斷t+0.5時(R,C)是否有煙霧，
# 煙霧在t時刻會從前一刻的位置移動過來
# 所以我們從(R,C)反向移動一步，判斷t-1時刻該位置是否有煙霧
rev_dir_map = {
    'N': (1, 0),
    'W': (0, 1),
    'S': (-1, 0),
    'E': (0, -1)
}

# 紀錄時間t時刻煙霧所在位置集合
# 初始時刻t=0，煙霧在(0,0)
smoke = {(0, 0)}

res = []

for t in range(1, N + 1):
    # 反向移動判斷(R,C)是否有煙霧
    dr, dc = rev_dir_map[S[t - 1]]
    prev_pos = (R + dr, C + dc)
    # 如果t-1時刻prev_pos有煙霧，則t+0.5時(R,C)有煙霧
    if prev_pos in smoke:
        res.append('1')
    else:
        res.append('0')

    # 煙霧移動
    ddr, ddc = dir_map[S[t - 1]]
    new_smoke = set()
    for (r, c) in smoke:
        new_smoke.add((r + ddr, c + ddc))

    # 如果(0,0)沒有煙霧，新增煙霧
    if (0, 0) not in new_smoke:
        new_smoke.add((0, 0))

    smoke = new_smoke

print(''.join(res))
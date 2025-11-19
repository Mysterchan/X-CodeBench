import sys
input = sys.stdin.readline

# 方向映射
dir_map = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

R_t, C_t, R_a, C_a = map(int, input().split())
N, M, L = map(int, input().split())

S = []
for _ in range(M):
    ch, cnt = input().split()
    cnt = int(cnt)
    S.append((ch, cnt))

T = []
for _ in range(L):
    ch, cnt = input().split()
    cnt = int(cnt)
    T.append((ch, cnt))

# 兩人移動序列的指標與剩餘長度
i, j = 0, 0
rem_s, rem_t = S[0][1], T[0][1]
ch_s, ch_t = S[0][0], T[0][0]

# 初始位置差距
dr = R_t - R_a
dc = C_t - C_a

ans = 0

while i < M and j < L:
    # 本輪移動長度為兩者剩餘中較小者
    length = min(rem_s, rem_t)

    # 本輪兩人移動方向向量
    dsr, dsc = dir_map[ch_s]
    dtr, dtc = dir_map[ch_t]

    # 差距每步變化量
    ddr = dsr - dtr
    ddc = dsc - dtc

    # 差距在本段的起點
    start_dr = dr
    start_dc = dc

    # 差距在本段的終點（移動 length 步後）
    end_dr = dr + ddr * length
    end_dc = dc + ddc * length

    # 計算本段中差距為0的步數
    # 差距隨步數 k 變化為 (start_dr + ddr*k, start_dc + ddc*k), k=1..length
    # 找 k 使得 start_dr + ddr*k = 0 且 start_dc + ddc*k = 0

    if ddr == 0 and ddc == 0:
        # 差距不變，若起點差距為0，整段都相同
        if start_dr == 0 and start_dc == 0:
            ans += length
    elif ddr == 0:
        # r方向差距不變，必須 start_dr=0 才可能相同
        if start_dr == 0:
            # c方向差距線性變化，找 k 使 start_dc + ddc*k=0
            # k = -start_dc / ddc
            if ddc != 0:
                k = -start_dc / ddc
                if k.is_integer() and 1 <= k <= length:
                    ans += 1
    elif ddc == 0:
        # c方向差距不變，必須 start_dc=0 才可能相同
        if start_dc == 0:
            # r方向差距線性變化，找 k 使 start_dr + ddr*k=0
            # k = -start_dr / ddr
            if ddr != 0:
                k = -start_dr / ddr
                if k.is_integer() and 1 <= k <= length:
                    ans += 1
    else:
        # ddr != 0 且 ddc != 0
        # 兩條方程必須同時成立
        # k = -start_dr / ddr = -start_dc / ddc
        # 先判斷是否相等
        if ddr * start_dc == ddc * start_dr:
            # k = -start_dr / ddr
            k = -start_dr / ddr
            if k.is_integer() and 1 <= k <= length:
                ans += 1

    # 更新差距
    dr = end_dr
    dc = end_dc

    # 更新剩餘長度與指標
    rem_s -= length
    rem_t -= length
    if rem_s == 0:
        i += 1
        if i < M:
            ch_s, rem_s = S[i]
    if rem_t == 0:
        j += 1
        if j < L:
            ch_t, rem_t = T[j]

print(ans)
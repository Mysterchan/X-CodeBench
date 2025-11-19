import sys
input = sys.stdin.readline

# 移動方向を座標変化に変換する辞書
dir_map = {
    'U': (-1, 0),
    'D': (1, 0),
    'L': (0, -1),
    'R': (0, 1),
}

R_t, C_t, R_a, C_a = map(int, input().split())
N, M, L = map(int, input().split())

S = []
for _ in range(M):
    d, a = input().split()
    a = int(a)
    S.append((d, a))

T = []
for _ in range(L):
    d, b = input().split()
    b = int(b)
    T.append((d, b))

# S, T の区間をそれぞれの移動方向のベクトルと長さで表す
# 例: S[i] = (dr, dc, length)
S_vec = []
for d, a in S:
    dr, dc = dir_map[d]
    S_vec.append((dr, dc, a))

T_vec = []
for d, b in T:
    dr, dc = dir_map[d]
    T_vec.append((dr, dc, b))

# ポインタと残り長さを使って、SとTの区間を同期的に処理する
i, j = 0, 0
len_i, len_j = S_vec[0][2], T_vec[0][2]
pos_t_r, pos_t_c = R_t, C_t
pos_a_r, pos_a_c = R_a, C_a

ans = 0

while i < M and j < L:
    # 今回処理する区間の長さは両方の区間の残りのうち小さい方
    length = min(len_i, len_j)

    # Sの移動ベクトル
    dr_s, dc_s, _ = S_vec[i]
    # Tの移動ベクトル
    dr_t, dc_t, _ = T_vec[j]

    # 高橋君と青木君の相対位置の変化ベクトル
    ddr = dr_s - dr_t
    ddc = dc_s - dc_t

    # 高橋君と青木君の現在の相対位置
    rr = pos_t_r - pos_a_r
    cc = pos_t_c - pos_a_c

    # 区間内で同じマスにいる回数を計算する
    # 区間内のk回目の移動後の相対位置は (rr + ddr*k, cc + ddc*k), k=1..length
    # これが (0,0) になる回数を求める

    if ddr == 0 and ddc == 0:
        # 相対位置が変わらないので、もし最初の相対位置が0ならlength回全て同じマス
        if rr == 0 and cc == 0:
            ans += length
        # そうでなければ0回
    else:
        # 連立方程式を解く
        # rr + ddr*k = 0 => k = -rr/ddr (if ddr != 0)
        # cc + ddc*k = 0 => k = -cc/ddc (if ddc != 0)
        # kは整数かつ 1 <= k <= length

        # kの候補を求める関数
        def valid_k(rr, ddr, cc, ddc):
            # ddr, ddc のどちらかが0の場合を考慮
            if ddr == 0 and ddc == 0:
                # ここは呼ばれないはず
                return []
            elif ddr == 0:
                # rr must be 0, else no solution
                if rr != 0:
                    return []
                # solve cc + ddc*k = 0
                if ddc == 0:
                    return []
                if (-cc) % ddc != 0:
                    return []
                k = (-cc) // ddc
                if 1 <= k <= length:
                    return [k]
                else:
                    return []
            elif ddc == 0:
                # cc must be 0, else no solution
                if cc != 0:
                    return []
                # solve rr + ddr*k = 0
                if ddr == 0:
                    return []
                if (-rr) % ddr != 0:
                    return []
                k = (-rr) // ddr
                if 1 <= k <= length:
                    return [k]
                else:
                    return []
            else:
                # 両方0でない場合
                # k = -rr/ddr = -cc/ddc かつ kは整数
                # まず kが整数か判定
                if (-rr) * ddc != (-cc) * ddr:
                    return []
                # k = -rr/ddr
                if (-rr) % ddr != 0:
                    return []
                k = (-rr) // ddr
                if 1 <= k <= length:
                    return [k]
                else:
                    return []

        ans += len(valid_k(rr, ddr, cc, ddc))

    # 移動後の位置を更新
    pos_t_r += dr_s * length
    pos_t_c += dc_s * length
    pos_a_r += dr_t * length
    pos_a_c += dc_t * length

    # 残り長さを減らす
    len_i -= length
    len_j -= length

    if len_i == 0:
        i += 1
        if i < M:
            len_i = S_vec[i][2]
    if len_j == 0:
        j += 1
        if j < L:
            len_j = T_vec[j][2]

print(ans)
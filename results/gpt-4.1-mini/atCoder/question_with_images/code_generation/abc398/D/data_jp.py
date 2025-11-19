import sys
input = sys.stdin.readline

N, R, C = map(int, input().split())
S = input().rstrip()

# 煙の移動方向の逆方向を考える
# 時刻 t+0.5 に (R,C) に煙がある ⇔ 時刻 t-0.5 に (R,C) の逆方向に移動したマスに煙があった
# 逆にたどることで、時刻 0.5 に (r0,c0) に煙があったかを判定できる
# 時刻 0.5 は (0,0) のみ煙がある

# 逆方向の移動ベクトル
rev_dir = {
    'N': (1, 0),
    'S': (-1, 0),
    'W': (0, 1),
    'E': (0, -1),
}

r, c = R, C
res = []
for i in range(N-1, -1, -1):
    dr, dc = rev_dir[S[i]]
    r += dr
    c += dc
    # 時刻 0.5 に (r,c) に煙があるか判定
    # 0.5時点では(0,0)のみ煙がある
    if r == 0 and c == 0:
        # ここから先は煙が存在するので、時刻 i+1 の t+0.5 に煙がある
        # それ以降はすべて1になる
        res.append('1')
        # 残りはすべて1
        res.extend(['1'] * i)
        break
    else:
        res.append('0')
else:
    # ループをbreakしなかった場合、すべて0
    pass

print(''.join(res[::-1]))
import sys
input = sys.stdin.readline

N, W = map(int, input().split())
blocks = [None] * N
cols = [[] for _ in range(W+1)]  # 1-indexed columns

for i in range(N):
    x, y = map(int, input().split())
    blocks[i] = (x, y)
    cols[x].append((y, i))

# 各列でy座標の降順にソート（上から下へ）
for c in range(1, W+1):
    cols[c].sort(reverse=True)

# 各列のブロックの消滅時刻を計算
# 消滅時刻は、ブロックが消える時刻（整数時刻）
# 消滅しない場合は INF (10^15で十分)
INF = 10**15
disappear = [INF] * N

# 各列で消滅時刻を計算
for c in range(1, W+1):
    col = cols[c]
    # colは(y, idx)の降順（上から下）
    # 下から1行目のy座標は最小のy
    # 消滅時刻は、下から1行目のy座標 + k - 1 (kはブロックの位置(1-based) from bottom)
    # ただし、k=1のブロックは最下行にいるので消滅時刻 = y_min
    # つまり、消滅時刻 = y_min + (k-1)
    # kは下からの順位なので、k=1は最下のブロック（y最小）
    # colは上から下なので逆順でkを割り当てる
    k = 1
    for y, idx in reversed(col):
        disappear[idx] = y + (k - 1)
        k += 1

Q = int(input())
for _q in range(Q):
    T, A = map(int, input().split())
    A -= 1
    # 時刻T+0.5に存在するか？
    # ブロックは時刻 disappear[A] に消滅
    # 時刻T+0.5 < disappear[A]なら存在
    # 時刻T+0.5 >= disappear[A]なら消滅済み
    # つまり T < disappear[A] なら Yes
    print("Yes" if T < disappear[A] else "No")
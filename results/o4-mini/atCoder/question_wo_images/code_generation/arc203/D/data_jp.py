import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# 問題の操作は、Bの隣接要素間にB_i XOR B_{i+1}を挿入する操作を繰り返してAにできるか、というもの。
# この操作は、Bの隣接要素のXORを挿入していくことで、Bの隣接要素のXOR列をAの隣接要素のXOR列に一致させることができる。
# つまり、Aの隣接要素のXOR列がBの隣接要素のXOR列と一致する必要がある。
# Bの長さを最小にするには、Bの隣接要素のXOR列がAの隣接要素のXOR列と一致し、かつBの長さは隣接XOR列の長さ+1。
# しかし、Bの隣接要素のXOR列はAの隣接要素のXOR列の「連続する同じ値の塊」を1つにまとめることができる。
# つまり、Aの隣接XOR列の連続する同じ値の塊の数 + 1 が最小のBの長さとなる。

# 具体的には、Aの隣接XOR列を考えると長さはN-1。
# その中で連続する同じ値の塊の数を数える。
# これに1を足したものが答え。

# クエリではAのある位置の値を反転させる。
# それにより隣接XOR列のいくつかの値が変わる可能性がある。
# 変わるのはi-1番目の隣接XOR（i>1の場合）とi番目の隣接XOR（i<Nの場合）。
# これらの変化により連続塊の数が変わるので、それを効率的に更新する必要がある。

# 連続塊の数を管理するために、隣接XOR列の各要素の値を保持し、
# それらの隣接要素との比較で塊の境界を判定する。
# 境界は隣接XOR列の隣接要素が異なる箇所。

# 連続塊の数 = 境界の数 + 1
# 境界の数は隣接XOR列の隣接要素間の異なる箇所の数。

# したがって、隣接XOR列の長さはN-1。
# 境界の数は0からN-2までの位置で、xor[i] != xor[i+1] の数。

# クエリでA[i]を反転すると、隣接XOR列のi-1番目とi番目が変わる可能性がある。
# それぞれの変化に対して境界の変化を更新する。

# 実装方針:
# 1. Aの隣接XOR列を作成
# 2. 境界の数を計算
# 3. クエリごとにA[i]を反転
# 4. 隣接XOR列のi-1番目とi番目を更新
# 5. 境界の数を更新
# 6. 答えは境界の数 + 1

# 境界の数の更新は、隣接XOR列の隣接要素の比較結果の変化を見て行う。

A = A
N = len(A)

# 隣接XOR列
xor = [A[i] ^ A[i+1] for i in range(N-1)]

# 境界の数を計算
# 境界はxor[i] != xor[i+1] の数 (i=0..N-3)
boundary = 0
for i in range(N-2):
    if xor[i] != xor[i+1]:
        boundary += 1

def update_boundary(pos):
    # posは境界の位置 (0 <= pos < N-2)
    # xor[pos] != xor[pos+1] の判定を行い、境界の数を更新する
    # 変更前後の比較を行うため、呼び出し元で管理する
    pass

# 境界の数を管理するため、境界の位置ごとにxor[pos] != xor[pos+1] の真偽を管理する
# 変更時に境界の真偽が変わるかを判定し、boundaryを増減する

# 境界の真偽を配列で管理
boundary_flags = [0]*(N-2)
for i in range(N-2):
    if xor[i] != xor[i+1]:
        boundary_flags[i] = 1

boundary = sum(boundary_flags)

for _ in range(Q):
    i = int(input()) - 1
    # A[i]を反転
    A[i] ^= 1

    # 隣接XOR列のi-1番目とi番目を更新
    # i-1番目はi-1とiの間のXOR => A[i-1]^A[i]
    if i - 1 >= 0:
        old = xor[i-1]
        xor[i-1] = A[i-1] ^ A[i]
        if old != xor[i-1]:
            # xor[i-1]が変わったので、境界の判定に影響するのは
            # i-2番目の境界 (xor[i-2] != xor[i-1]) と
            # i-1番目の境界 (xor[i-1] != xor[i]) の2箇所
            # それぞれ存在すれば更新する

            # i-2番目の境界
            if i - 2 >= 0:
                old_flag = boundary_flags[i-2]
                new_flag = 1 if xor[i-2] != xor[i-1] else 0
                if old_flag != new_flag:
                    boundary_flags[i-2] = new_flag
                    boundary += new_flag - old_flag

            # i-1番目の境界
            if i - 1 < N - 2:
                old_flag = boundary_flags[i-1]
                new_flag = 1 if xor[i-1] != xor[i] else 0
                if old_flag != new_flag:
                    boundary_flags[i-1] = new_flag
                    boundary += new_flag - old_flag

    # i番目の隣接XOR列
    if i < N - 1:
        old = xor[i]
        xor[i] = A[i] ^ A[i+1]
        if old != xor[i]:
            # i-1番目の境界 (xor[i-1] != xor[i]) と
            # i番目の境界 (xor[i] != xor[i+1]) の2箇所を更新

            # i-1番目の境界
            if i - 1 >= 0:
                old_flag = boundary_flags[i-1]
                new_flag = 1 if xor[i-1] != xor[i] else 0
                if old_flag != new_flag:
                    boundary_flags[i-1] = new_flag
                    boundary += new_flag - old_flag

            # i番目の境界
            if i < N - 2:
                old_flag = boundary_flags[i]
                new_flag = 1 if xor[i] != xor[i+1] else 0
                if old_flag != new_flag:
                    boundary_flags[i] = new_flag
                    boundary += new_flag - old_flag

    # 答えは境界の数 + 1
    print(boundary + 1)
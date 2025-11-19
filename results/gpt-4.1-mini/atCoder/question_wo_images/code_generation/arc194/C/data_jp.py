import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 初期のAのコスト
cost = sum(a * c for a, c in zip(A, C))

# AとBが一致しているかどうか
if A == B:
    print(0)
    exit()

# AとBが異なる位置の集合
diff_indices = [i for i in range(N) if A[i] != B[i]]

# 操作回数はdiff_indicesの長さ
# 操作の順序を工夫してコストを最小化する必要がある

# 操作の性質を考察
# 操作は1回につき1つのビットを反転し、その後のAのコストを支払う
# 反転したビットはA[i]が0->1または1->0に変わる
# 反転したビットのコスト変化は ±C[i]
# 反転操作のコストは反転後のAのコストの合計

# 反転すべきビットはdiff_indicesの位置のみ
# 反転操作の順序を決めることで合計コストが変わる

# 反転操作のコストは、反転後のAのコストの合計
# 反転操作を行うたびにAのコストは ±C[i] 変化する

# 反転操作のコストの合計は
# 初期コスト + Σ(操作後のAのコストの変化分)

# 反転操作の順序を決める問題は、差分のC[i]の符号を考慮して
# 反転操作のコストの合計を最小化する順序を求める問題に帰着する

# 具体的には、反転操作のコストは
# 初期コスト + Σ_{k=1}^{M} (初期コスト + Σ_{j=1}^k Δ_j)
# ここでΔ_jはj回目の反転操作によるAのコストの変化（±C[i_j]）

# これを展開すると
# 合計コスト = M * 初期コスト + Σ_{k=1}^M Σ_{j=1}^k Δ_j
# = M * 初期コスト + Σ_{j=1}^M (M - j + 1) * Δ_j

# Δ_jは反転するビットi_jのC[i_j]の符号反転分
# 反転するビットiのΔは ±C[i]
# 反転するビットiはA[i]とB[i]が異なるので
# A[i] = 0, B[i] = 1 の場合、反転で0->1なのでΔ = +C[i]
# A[i] = 1, B[i] = 0 の場合、反転で1->0なのでΔ = -C[i]

# したがって、Δ_i = C[i] if A[i] == 0 else -C[i]

# 合計コストを最小化するために、Δ_iの大きいものを後ろに置くか前に置くかを考える
# Σ_{j=1}^M (M - j + 1) * Δ_j を最小化するには
# Δ_jが正のものは重み(M - j + 1)が小さい位置に置きたい（後ろに置く）
# Δ_jが負のものは重みが大きい位置に置きたい（前に置く）

# つまり、Δ_i < 0 のものを前に、Δ_i > 0 のものを後ろに並べる
# Δ_i = 0 はない（C[i] >= 1）

# Δ_i < 0 のものは大きい負の値から小さい負の値へ（絶対値の大きい順）に並べるのが良い
# Δ_i > 0 のものは小さい正の値から大きい正の値へ並べるのが良い

# これにより、合計コストが最小化される

# まとめ:
# 1. Δ_i < 0 のものを絶対値の大きい順に前に並べる
# 2. Δ_i > 0 のものを小さい順に後ろに並べる

# これが反転操作の順序

delta = []
for i in diff_indices:
    d = C[i] if A[i] == 0 else -C[i]
    delta.append((d, i))

neg = [x for x in delta if x[0] < 0]
pos = [x for x in delta if x[0] > 0]

# negは絶対値の大きい順にソート（負の値なので昇順）
neg.sort(key=lambda x: x[0])  # 負の値が小さい順（絶対値大きい順）
# posは小さい順にソート
pos.sort(key=lambda x: x[0])

order = neg + pos

# 合計コスト計算
# 初期コスト
init_cost = cost
M = len(order)

# Δのリスト
D = [d for d, _ in order]

# 合計コスト = M * init_cost + Σ_{j=1}^M (M - j + 1) * D_j
# jは1-indexedなので注意

ans = M * init_cost
for j, d in enumerate(D, 1):
    ans += (M - j + 1) * d

print(ans)
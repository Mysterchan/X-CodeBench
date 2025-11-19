import sys
input = sys.stdin.readline

N, M = map(int, input().split())
P = list(map(int, input().split()))

# 各商品の単価P_iに対して、k個買うと k^2 * P_i 円かかる。
# 目的: 合計金額 <= M のとき、購入個数の最大値を求める。

# k_i個買うときのコストは k_i^2 * P_i
# 合計コスト = sum(k_i^2 * P_i) <= M
# k_i >= 0

# ここで、k_iは整数。

# 目的は sum(k_i) を最大化すること。

# 重要な点:
# - 各商品のコストは k_i^2 * P_i
# - P_i > 0
# - k_iは0以上の整数

# これを満たす最大の sum(k_i) を求める。

# 方針:
# 二分探索で「購入個数の合計をx個にできるか」を判定する。

# 判定関数:
# ある合計個数xを買うために、各商品に割り振る個数k_iを決める。
# しかし、k_iは整数で、sum(k_i) = x。
# コストを最小化するためには、コスト効率の良い商品に多く割り振るべき。

# しかし、コストは k_i^2 * P_i で、k_iが大きくなるとコストは二次関数的に増える。

# ここで、コストを最小化するk_iの割り振りは、Lagrangeの未定乗数法で求められる。

# 連続値で考えると、k_iは実数で、
# 制約 sum k_i = x
# コスト最小化は
# min sum P_i * k_i^2 s.t. sum k_i = x, k_i >= 0

# ラグランジュの条件から、
# k_i = λ / (2 * P_i)
# sum k_i = x => sum λ/(2*P_i) = x => λ = 2x / sum(1/P_i)
# よって k_i = x / sum(1/P_j) * 1/P_i

# つまり、k_i は比例配分される。

# しかし k_iは整数なので、k_iを整数に丸める必要がある。

# そこで、k_iの候補は floor(k_i_real) または ceil(k_i_real) のどちらか。

# 判定関数では、k_i_realを計算し、floorで割り当てた個数の合計をsum_floorとする。
# sum_floor <= x であれば、残りの個数をceilにして調整する。

# しかし、コストは k_i^2 * P_i なので、k_iを増やすとコストが増える。

# そこで、k_iをfloorからceilに増やすときのコスト増分を計算し、
# コスト増分が小さい順にceilにしていく。

# これにより、合計個数xを割り振ったときの最小コストを求められる。

# 判定関数の実装手順:
# 1. 各iについて k_i_real = x / sum(1/P_j) * 1/P_i
# 2. floor_k_i = floor(k_i_real)
# 3. sum_floor = sum floor_k_i
# 4. diff = x - sum_floor (diff >= 0)
# 5. cost_floor = sum floor_k_i^2 * P_i
# 6. cost_increments = [( (floor_k_i+1)^2 - floor_k_i^2 ) * P_i for i]
# 7. cost_incrementsを昇順にソートし、diff個分だけ足す
# 8. total_cost = cost_floor + sum of diff smallest cost_increments
# 9. total_cost <= M なら x個買うことが可能

# ただし、sum(1/P_i) は計算時に浮動小数点誤差が出る可能性があるので、
# 十分な精度で計算する。

# また、k_i_realは非常に小さいかもしれないので、0個買うこともある。

# さらに、k_i_realが非常に大きくなることもあるが、k_iは整数なので問題ない。

# これで二分探索を行う。

# 二分探索の範囲:
# 最小0個、最大は理論上無限大だが、M <= 10^18なので、
# 最大個数は sqrt(M / min(P_i)) * N 程度が上限。

# ただし、最大個数は M / min(P_i) の平方根のN倍程度。

# ここでは、最大個数の上限を 2*10^9 * 2*10^5 = 4*10^14 は大きすぎる。

# しかし、k_i^2 * P_i <= M なので、k_i <= sqrt(M / P_i)

# 各商品の最大個数は sqrt(M / P_i)

# 合計最大個数は sum sqrt(M / P_i)

# これを計算して上限にする。

import math

invP_sum = 0.0
for p in P:
    invP_sum += 1.0 / p

def can_buy(x):
    # x個買うときの最小コストを計算
    # k_i_real = x / invP_sum * 1/P_i
    # floor_k_i = int(k_i_real)
    # diff = x - sum floor_k_i
    # cost_floor = sum floor_k_i^2 * P_i
    # cost_increments = ((floor_k_i+1)^2 - floor_k_i^2) * P_i
    # diff個分だけcost_incrementsの小さい順に足す
    k_real = []
    floor_k = []
    cost_floor = 0
    cost_increments = []
    sum_floor = 0
    base = x / invP_sum
    for i in range(N):
        kr = base / P[i]
        fk = int(kr)
        floor_k.append(fk)
        sum_floor += fk
        cost_floor += fk * fk * P[i]
        inc = ((fk + 1) * (fk + 1) - fk * fk) * P[i]
        cost_increments.append(inc)
    diff = x - sum_floor
    if diff < 0:
        # floor_kの合計がxを超えることは理論上ないが念のため
        return False
    cost_increments.sort()
    total_cost = cost_floor + sum(cost_increments[:diff])
    return total_cost <= M

# 最大個数の上限を計算
max_k = 0
for p in P:
    max_k += int(math.isqrt(M // p))  # 各商品の最大個数の合計

left, right = 0, max_k
ans = 0
while left <= right:
    mid = (left + right) // 2
    if can_buy(mid):
        ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
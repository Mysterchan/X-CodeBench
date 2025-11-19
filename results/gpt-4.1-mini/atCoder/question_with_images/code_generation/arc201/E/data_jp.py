MOD = 998244353

import sys
input = sys.stdin.readline

N = int(input())
Y = list(map(int, input().split()))

# Yは1..Nの順列
# 点iの座標は (i, Y_i)

# 部分集合Sのバウンディングボックスの面積は
# (max_x - min_x) * (max_y - min_y)
# ここでx座標はiの範囲、y座標はY_iの範囲

# 全ての2以上の部分集合Sに対して面積の総和を求める

# 面積 = (max_x - min_x) * (max_y - min_y)
# = (max_x - min_x) * (max_y - min_y)
# x座標は点番号の範囲なので、xの差は区間の長さ - 1
# y座標はY_iの値の範囲

# 重要な点:
# Yは1..Nの順列なので、Y_iは全て異なる値

# 部分集合のx座標のmin,maxは点番号のmin,max
# 部分集合のy座標のmin,maxはY_iのmin,max

# 部分集合のx座標のmin,maxは区間の端点のiの値
# 部分集合のy座標のmin,maxはY_iの値のmin,max

# 部分集合は任意の2以上の点の集合なので、x座標のmin,maxは任意のi,j (i<j)の組み合わせで決まる区間[i,j]
# つまり、x座標の範囲は区間[i,j]の長さ = j - i

# y座標のmin,maxは区間[i,j]のY_iの値のmin,max

# つまり、全ての区間[i,j] (1 <= i < j <= N)について
# 面積 = (j - i) * (max_{k=i..j} Y_k - min_{k=i..j} Y_k)
# の総和を求めることと同じ

# これを全区間で計算するのはO(N^2)で無理

# そこで、yの最大値と最小値の差の総和を効率的に求める方法を考える

# 面積の総和 = Σ_{1 <= i < j <= N} (j - i) * (maxY - minY)

# = Σ_{1 <= i < j <= N} (j - i) * maxY - Σ_{1 <= i < j <= N} (j - i) * minY

# maxYの部分とminYの部分に分けて考える

# maxYの部分の総和 = Σ_{区間} (区間長) * maxY
# minYの部分の総和 = Σ_{区間} (区間長) * minY

# これらはそれぞれ「区間の最大値の総和」と「区間の最小値の総和」に区間長を掛けたものの総和

# ここで、区間長 = j - i

# つまり、区間の最大値の総和に区間長を掛けて合計する

# これを効率的に計算するには、区間の最大値の総和と区間の最小値の総和を別々に計算し、
# それぞれに区間長を掛けて合計する方法を考える

# しかし、区間長を掛けるのは難しいので、別のアプローチを考える

# 代わりに、maxYとminYの差の総和を区間長で重み付けして合計する

# ここで、区間長 = j - i

# 重要なことは、Yは1..Nの順列なので、Yの値は一意に点を特定できる

# そこで、maxYとminYの差の総和を区間長で重み付けて合計する問題を
# maxYの総和とminYの総和に分けて考える

# maxYの総和（区間長重み付き）を計算する方法:
# Yの値が最大となる区間を考える
# Yの値がvの点の位置はpos[v] = i (Y_i = v)

# vが区間の最大値となる区間は、vより大きい値の位置によって区間が制限される

# つまり、vより大きい値の位置の左右の境界の間の区間でvが最大値となる

# 同様にminYの総和も同様に計算できる

# これを利用して、maxYの総和とminYの総和を計算し、
# それらの差をとることで求める

# 具体的には、モノトニックスタックを使って
# 各値が最大値または最小値となる区間を求める

# さらに、区間長の重みを考慮して計算する

# 参考: AtCoder Typical DP Contestや類似問題の区間最大・最小値の総和の計算方法

# ここでは、区間長を重みとした区間最大値の総和を計算する方法を示す

# 1. Yの値の位置をpos[v]として記録
pos = [0]*(N+1)
for i, y in enumerate(Y,1):
    pos[y] = i

# 2. maxYの総和を計算
# vが最大値となる区間の左右境界を求める
# vより大きい値の位置を使って区間を区切る

# 大きい値の位置を管理するために、vを大きい順に処理
# 位置をソートして管理

# 3. minYの総和も同様に計算

# 4. 最終的に Σ (区間長 * maxY) - Σ (区間長 * minY) を計算

# 5. x座標の差は区間長 = j - i

# 6. ただし、区間長は j - i なので、区間の長さは (右 - 左) であることに注意

# 7. 区間の長さを使って計算するために、区間の数え方を工夫する

# 以下に実装

# 区間長を重みとした区間最大値の総和の計算関数
def calc_sum(arr):
    # arrはYの値の配列
    # arrは1..Nの順列
    # pos[v]はvの位置
    # vが最大値となる区間の左右境界を求める
    # vより大きい値の位置を使って区間を区切る

    # 大きい値の位置を管理するために、vを大きい順に処理
    # 位置をソートして管理

    # 位置のリストに0とN+1を追加して境界とする
    pos_list = [0] + sorted(pos[1:]) + [N+1]

    # vの位置
    # vが最大値となる区間は、vの位置を含み、vより大きい値の位置の間の区間
    # つまり、vの位置の左右の大きい値の位置を見つける

    # 位置の配列を使ってvの位置の左右の境界を二分探索で求める

    import bisect

    res = 0
    for v in range(1, N+1):
        p = pos[v]
        # pの左右の大きい値の位置を探す
        idx = bisect.bisect_left(pos_list, p)
        left = pos_list[idx-1]
        right = pos_list[idx]

        # vが最大値となる区間は [l, r] で left < l <= p <= r < right
        # 区間の数は (p - left) * (right - p)
        # ここで区間長 = r - l
        # 区間長の総和を計算する

        # 区間長の総和 = Σ_{l=left+1}^{p} Σ_{r=p}^{right-1} (r - l)
        # = Σ_{l=left+1}^{p} Σ_{r=p}^{right-1} (r) - Σ_{l=left+1}^{p} Σ_{r=p}^{right-1} (l)
        # = (p - left) * Σ_{r=p}^{right-1} r - (right - p) * Σ_{l=left+1}^{p} l

        count_left = p - left
        count_right = right - p

        # Σ_{r=a}^{b} r = (b*(b+1)//2) - ((a-1)*a//2)
        sum_r = (right - 1)*right//2 - (p - 1)*p//2
        sum_l = p*(p+1)//2 - left*(left+1)//2

        total = count_left * sum_r - count_right * sum_l
        res += v * total
    return res % MOD

# maxYの総和
max_sum = calc_sum(Y)

# minYの総和はYの値を反転させて計算
# minYの総和 = Σ (区間長 * minY)
# minYの最大値の総和として計算できる

# Yの値を反転
Y_inv = [N+1 - y for y in Y]

# posを再計算
pos = [0]*(N+1)
for i, y in enumerate(Y_inv,1):
    pos[y] = i

min_sum = calc_sum(Y_inv)

ans = (max_sum - min_sum) % MOD
print(ans)
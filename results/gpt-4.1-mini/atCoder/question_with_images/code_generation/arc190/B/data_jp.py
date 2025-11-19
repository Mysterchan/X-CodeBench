import sys
input = sys.stdin.readline
MOD = 998244353

N, a, b = map(int, input().split())
Q = int(input())
ks = list(map(int, input().split()))

# 各レベル k に対して、(a,b) がレベル k の L 型に含まれる方法の個数を求める。
# 問題の定義より、レベル k の L 型は4種類の形があり、
# それぞれの形の中心マス (i,j) の取りうる範囲が決まっている。
# (a,b) がレベル k の L 型に含まれるためには、
# その L 型 の中心 (i,j) が (a,b) を含むように選べる必要がある。
#
# 4つの形の中心 (i,j) の範囲は以下の通り：
# 1) i in [1, N-k+1], j in [1, N-k+1]
# 2) i in [1, N-k+1], j in [k, N]
# 3) i in [k, N], j in [1, N-k+1]
# 4) i in [k, N], j in [k, N]
#
# (a,b) が含まれる条件はそれぞれの形で異なる。
# 例えば形1は (i,j) から右または下に0～k-1マス進んだマスの集合なので、
# (a,b) が含まれるには i ≤ a ≤ i+k-1, j ≤ b ≤ j+k-1 となる。
# これを i,j の範囲と合わせて考えると、
# i ∈ [max(1, a-k+1), min(a, N-k+1)]
# j ∈ [max(1, b-k+1), min(b, N-k+1)]
# この範囲の中心 (i,j) の個数が形1の該当数。
#
# 同様に形2,3,4も計算し、4つの形の該当数の和が答え。
#
# ただし、問題文の「1つ以上に該当するもの」とあるので重複はカウントしない。
# しかし、4つの形は互いに重複しない（L型の定義上、中心の範囲が互いに排反）。
# よって単純に4つの個数を足せばよい。
#
# 最後に、全レベルのL型の分割方法はそれぞれ独立に選べるため、
# レベルkのL型の選び方の数は上記の個数。
#
# これをQ回計算するが、Nが最大1e7でQ最大2e5なので、
# O(Q)で計算可能。

def count_range(l, r):
    return max(0, r - l + 1)

for k in ks:
    # 形1
    i1_l = max(1, a - k + 1)
    i1_r = min(a, N - k + 1)
    j1_l = max(1, b - k + 1)
    j1_r = min(b, N - k + 1)
    c1 = count_range(i1_l, i1_r) * count_range(j1_l, j1_r)

    # 形2
    i2_l = max(1, a - k + 1)
    i2_r = min(a, N - k + 1)
    j2_l = max(k, b)
    j2_r = min(N, b + k - 1)
    c2 = count_range(i2_l, i2_r) * count_range(j2_l, j2_r)

    # 形3
    i3_l = max(k, a)
    i3_r = min(N, a + k - 1)
    j3_l = max(1, b - k + 1)
    j3_r = min(b, N - k + 1)
    c3 = count_range(i3_l, i3_r) * count_range(j3_l, j3_r)

    # 形4
    i4_l = max(k, a)
    i4_r = min(N, a + k - 1)
    j4_l = max(k, b)
    j4_r = min(N, b + k - 1)
    c4 = count_range(i4_l, i4_r) * count_range(j4_l, j4_r)

    ans = (c1 + c2 + c3 + c4) % MOD
    print(ans)
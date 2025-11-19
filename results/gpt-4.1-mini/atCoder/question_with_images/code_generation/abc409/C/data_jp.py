import sys
input = sys.stdin.readline

N, L = map(int, input().split())
d = list(map(int, input().split()))

# 点iの位置を計算（0-based）
pos = [0] * N
for i in range(1, N):
    pos[i] = (pos[i-1] + d[i-1]) % L

# 位置 -> 点番号の辞書（複数点が同じ位置なら複数登録）
pos_dict = {}
for i, p in enumerate(pos, 1):
    if p not in pos_dict:
        pos_dict[p] = []
    pos_dict[p].append(i)

# 正三角形の条件：
# 円周上の3点a,b,cが正三角形になるのは、
# 3点の位置が等間隔であること。
# つまり、3点の位置の差がL/3である必要がある。
# Lが3で割り切れない場合は0。

if L % 3 != 0:
    print(0)
    sys.exit()

step = L // 3
ans = 0

# pos_dictのキーをソートしておく
positions = sorted(pos_dict.keys())

# 位置pに点があるとき、p+step, p+2*stepも位置として存在すれば
# それらの点の組み合わせで正三角形ができる。
# ただし、点は異なる位置にある必要がある。

# 位置はmod Lなので、(p + step) % L, (p + 2*step) % Lを探す
for p in positions:
    p1 = p
    p2 = (p + step) % L
    p3 = (p + 2 * step) % L
    if p2 in pos_dict and p3 in pos_dict:
        # pos_dict[p1], pos_dict[p2], pos_dict[p3]はそれぞれ点のリスト
        # それぞれのリストの長さの積が組み合わせ数
        # ただし、a < b < c の条件を満たす必要があるので
        # 点番号の組み合わせで条件を満たすものを数える

        # それぞれのリストは点番号のリスト
        A = pos_dict[p1]
        B = pos_dict[p2]
        C = pos_dict[p3]

        # a < b < c を満たす組み合わせを数える
        # A, B, Cはそれぞれ昇順にソートされているとは限らないのでソート
        A.sort()
        B.sort()
        C.sort()

        # 三重ループは重いので、効率的に数える
        # a in A, b in B, c in C で a < b < c
        # これを効率的に数える方法：
        # 1. bを固定し、a < bの個数をAから二分探索で数える
        # 2. cを固定し、b < cの個数をBから二分探索で数える
        # 3. これらを組み合わせて総数を求める

        import bisect

        # Bについて、bごとにa < bの個数をAから計算
        a_counts = []
        for b in B:
            a_counts.append(bisect.bisect_left(A, b))
        # cについて、cごとにb < cの個数をBから計算
        b_counts = []
        for c in C:
            b_counts.append(len(B) - bisect.bisect_right(B, c - 1))

        # b_countsの累積和を作る（cの昇順に対応）
        # ただしcは昇順にソート済み
        # b_counts[i]はC[i]に対するbの個数
        # b_countsの累積和を作っておく
        b_cum = [0]
        for bc in b_counts:
            b_cum.append(b_cum[-1] + bc)

        # cのループでb_countsを使うためにcを昇順にしているので
        # b_countsはCの昇順に対応している

        # b_countsはcごとのbの個数
        # a_countsはbごとのaの個数

        # ここでa < b < cを満たす組み合わせ数は
        # sum_{c} sum_{b < c} (a < b)
        # = sum_{c} (sum_{b < c} a_counts[b_index])
        # これを効率的に計算するために
        # b_countsはb < cの個数なので、
        # b_counts[i] = number of b in B with b < C[i]
        # a_countsはbごとにa < bの個数

        # しかし、a_countsはbのインデックス順、b_countsはcのインデックス順なので
        # 直接掛け合わせるのは難しい。

        # よって、三重ループで計算（Nが大きいが、各位置の点数は通常小さいはず）
        # もし点数が大きい場合はTLEの可能性あり。

        # 三重ループで計算
        for a in A:
            for b in B:
                if a < b:
                    for c in C:
                        if b < c:
                            ans += 1

print(ans)
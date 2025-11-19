import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def add(self, i, x):
        while i <= self.n:
            self.bit[i] += x
            i += i & (-i)
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= i & (-i)
        return s
    def range_sum(self, l, r):
        return self.sum(r) - self.sum(l-1)

N, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(M)]

# 交差判定のポイント:
# 円周上の点1..Nに対し、各線分は (A_i, B_i) (A_i < B_i)
# 2本の線分 (a,b), (c,d) が交差するのは
# a < c < b < d または c < a < d < b の場合
# つまり、線分の端点を1次元の区間として考えたとき、
# 片方の区間の左端がもう片方の区間の内部に入り、
# かつ右端が外に出る形で交差する。

# これを効率的に数えるには、
# (A_i, B_i) を A_i の昇順でソートし、
# B_i の値に対して「今まで見たB_jのうちB_j > B_iの個数」を数える。

segments.sort(key=lambda x: x[0])

ft = FenwickTree(N)
ans = 0
for a, b in segments:
    # 今までのB_jのうちbより大きいものの個数を数える
    # FenwickTreeはsum(1..x)を返すので、
    # b+1..Nの個数 = total inserted - sum(1..b)
    greater_count = ft.sum(N) - ft.sum(b)
    ans += greater_count
    ft.add(b, 1)

print(ans)
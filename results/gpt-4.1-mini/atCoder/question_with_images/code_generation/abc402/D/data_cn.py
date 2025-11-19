import sys
input = sys.stdin.readline

# 线段 (A_i, B_i) 在圆上，A_i < B_i
# 两条线段 (a,b) 和 (c,d) 相交的条件是：
# a < c < b < d 或 c < a < d < b
# 也就是说，两个线段的端点交叉排列。

# 题目中给出 M 条线段，求满足 i<j 且线段 i 和 j 相交的对数。

# 解决方案：
# 1. 将所有线段按左端点升序排序。
# 2. 对于每条线段 (a,b)，统计之前所有线段中右端点 > b 的数量。
#    因为左端点是升序的，若当前线段是 (a,b)，之前线段的左端点都小于 a。
#    若之前线段的右端点 > b，则说明存在 (a',b')，a' < a 且 b' > b，
#    满足 a' < a < b < b'，即相交。
# 3. 统计所有这样的对数即为答案。

# 关键是如何高效统计之前线段中右端点 > b 的数量。
# 由于右端点范围是 [1, N]，N 最大 10^6，可以用 BIT（Fenwick Tree）或线段树。
# 这里用 BIT。

class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0]*(n+1)
    def update(self, i, v=1):
        while i <= self.n:
            self.tree[i] += v
            i += i & (-i)
    def query(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s
    def query_range(self, l, r):
        return self.query(r) - self.query(l-1)

N, M = map(int, input().split())
segments = [tuple(map(int, input().split())) for _ in range(M)]

# 按左端点升序排序
segments.sort(key=lambda x: x[0])

bit = BIT(N)
res = 0
for a, b in segments:
    # 统计之前右端点 > b 的数量
    # 即总数 - 右端点 ≤ b 的数量
    count_le_b = bit.query(b)
    count_all = bit.query(N)
    res += count_all - count_le_b
    bit.update(b)

print(res)
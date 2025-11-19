import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 先對 A 做離散化，方便後續使用
vals = sorted(set(A))
val_to_idx = {v: i for i, v in enumerate(vals)}

# 對 A 轉成離散後的索引
A_idx = [val_to_idx[a] for a in A]

# 構造一個長度為 N 的 LIS 長度前綴陣列，使用經典 O(N log N) LIS 算法
# tails[i] 表示長度為 i+1 的 LIS 的最小結尾元素值（離散後的索引）
tails = []
LIS_len_prefix = [0] * N
for i in range(N):
    pos = bisect.bisect_left(tails, A_idx[i])
    if pos == len(tails):
        tails.append(A_idx[i])
    else:
        tails[pos] = A_idx[i]
    LIS_len_prefix[i] = pos + 1

# 由於查詢中有條件 X_i，限制元素最大值 ≤ X_i，
# 我們需要能快速查詢在前 R_i 個元素中，且元素值 ≤ X_i 的 LIS 長度。

# 思路：
# 對於每個元素 A[i]，它對 LIS 的貢獻是基於它的值和位置。
# 我們需要一個資料結構，能在前 R_i 個元素中，對元素值 ≤ X_i 查詢 LIS 長度。

# 解法：
# 對元素值離散後的索引建立一個線段樹或 Fenwick Tree (BIT)，
# 用來維護 LIS 長度的最大值。
# 但因為查詢是對前 R_i 個元素，我們需要能對前綴做查詢。

# 因此，我們用 offline 查詢：
# 1. 將查詢按 R_i 排序。
# 2. 從左到右遍歷 A，更新 Fenwick Tree，記錄以 A[i] 為結尾的 LIS 長度。
# 3. 當遍歷到 R_i 時，對 Fenwick Tree 查詢 ≤ X_i 的最大 LIS 長度。

# Fenwick Tree 用於查詢離散值 ≤ X_i 的最大 LIS 長度。

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
    def update(self, i, v):
        i += 1
        while i <= self.n:
            if self.data[i] < v:
                self.data[i] = v
            i += i & (-i)
    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            if self.data[i] > res:
                res = self.data[i]
            i -= i & (-i)
        return res

# 將查詢離線，排序
queries = []
for i in range(Q):
    R, X = map(int, input().split())
    # X 也離散化，找出 X 在 vals 中的位置
    # 因為 X_i ≥ min{A_1..A_R}, X_i ≤ 10^9，且 vals 已排序
    # 找 X_i 在 vals 中的右邊界索引 (<= X_i)
    pos = bisect.bisect_right(vals, X) - 1
    queries.append((R, pos, i))

queries.sort(key=lambda x: x[0])  # 按 R 排序

fenw = Fenwick(len(vals))
res = [0] * Q

cur = 0
for R, pos, idx in queries:
    # 將 A[cur..R-1] 的元素更新到 fenw
    while cur < R:
        # 查詢 fenw 中 A[cur] - 1 的最大 LIS 長度
        prev_len = fenw.query(A_idx[cur] - 1) if A_idx[cur] > 0 else 0
        fenw.update(A_idx[cur], prev_len + 1)
        cur += 1
    # 查詢 ≤ pos 的最大 LIS 長度
    res[idx] = fenw.query(pos)

print('\n'.join(map(str, res)))
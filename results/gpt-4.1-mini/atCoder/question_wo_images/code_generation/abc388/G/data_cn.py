import sys
import bisect

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
Q = int(input())

# A 已排序，對每個查詢 (L,R)，我們要找最大 K，使得
# 在 A[L-1:R] 中，能配對 K 對 (a,b)，且 a <= b/2

# 配對策略：
# 對子序列 A[L-1:R]，長度 M = R-L+1
# 嘗試配對 K 對：
# 將前 K 個作為小麻糬，後 K 個作為大麻糬
# 對每個 i in [0,K-1]，檢查 A[L-1+i] <= A[L-1+M-K+i] / 2
# 若全部成立，則 K 可行

# 對每個查詢用二分法找最大 K

for _ in range(Q):
    L, R = map(int, input().split())
    length = R - L + 1
    left = 0
    right = length // 2
    res = 0
    base = L - 1
    while left <= right:
        mid = (left + right) // 2
        # 檢查 mid 對是否可行
        ok = True
        for i in range(mid):
            if A[base + i] * 2 > A[base + length - mid + i]:
                ok = False
                break
        if ok:
            res = mid
            left = mid + 1
        else:
            right = mid - 1
    print(res)